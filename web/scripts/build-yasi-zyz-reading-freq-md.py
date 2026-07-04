#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 ZYZ 阅读 PDF 语料统计考频词/短语，生成 Markdown。"""
from __future__ import annotations

import json
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

try:
    import fitz
except ImportError:
    print("需要 pymupdf: pip install pymupdf", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = Path(__file__).resolve().parent
PDF_DIR = Path(r"e:\BaiduNetdiskDownload\ZYZ\PDF")
YASI = ROOT / "content" / "posts" / "Yasi.md"
CACHE = SCRIPTS / "_yasi_zyz_corpus_cache.json"
OUT = ROOT / "content" / "posts" / "Yasi-ZYZ-阅读考频.md"
ZH_CACHE = SCRIPTS / "_yasi_en_zh_cache.json"
MIN_WORDS = 1000

try:
    import importlib.util

    _extra_spec = importlib.util.spec_from_file_location(
        "yasi_zyz_zh_extra", SCRIPTS / "_yasi_zyz_zh_extra.py"
    )
    _extra_mod = importlib.util.module_from_spec(_extra_spec)
    assert _extra_spec.loader is not None
    _extra_spec.loader.exec_module(_extra_mod)
    EXTRA_ZH: dict[str, str] = _extra_mod.EXTRA_ZH
except Exception:
    EXTRA_ZH = {}

PLURAL_KEEP = {
    "species", "series", "means", "works", "statistics", "politics", "economics",
    "news", "thanks", "headquarters", "physics", "mathematics", "ethics", "goods",
}
IRREGULAR: dict[str, str] = {
    "analyses": "analysis", "analysi": "analysis", "processes": "process", "processe": "process",
    "themselves": "they", "themselve": "they", "ourselves": "we", "ourselve": "we",
    "whereas": "whereas", "wherea": "whereas", "studies": "study", "bodies": "body",
    "feet": "foot", "mice": "mouse", "children": "child", "men": "man", "women": "woman",
    "emphasi": "emphasis", "hypothesi": "hypothesis", "photosynthesi": "photosynthesis",
    "synthesi": "synthesis", "thesi": "thesis", "oversea": "overseas",
}

EXAM_NOISE = re.compile(
    r"reading passage|you should spend|questions?\s+\d|choose the correct|"
    r"write your answers|answer sheet|ielts|true/false/not given|"
    r"yes/no/not given|matching headings|complete the summary|"
    r"list of headings|which paragraph contains|"
    r"do not write|no more than|words and/or|"
    r"copyright|all rights reserved|compiled|formatted|proofread|"
    r"commercial use|educational purposes|reproduced|permission|"
    r"boxes?\s+\d|write\s+true|write\s+yes|write\s+no|"
    r"end of questions|turn over|sample answer",
    re.I,
)
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")

STOP = {
    "about", "above", "across", "after", "again", "against", "also", "although", "always",
    "among", "another", "any", "anyone", "anything", "around", "away", "back", "because",
    "been", "before", "being", "below", "between", "both", "but", "came", "can", "cannot",
    "come", "could", "did", "does", "doing", "done", "down", "during", "each", "either",
    "else", "even", "every", "few", "first", "for", "found", "from", "further", "get",
    "give", "given", "go", "going", "gone", "got", "had", "has", "have", "having", "her",
    "here", "hers", "him", "his", "how", "however", "into", "its", "just", "keep", "know",
    "known", "last", "later", "least", "less", "like", "made", "make", "makes", "making",
    "many", "may", "might", "more", "most", "much", "must", "need", "never", "next", "not",
    "now", "off", "often", "once", "one", "only", "other", "others", "our", "out", "over",
    "own", "part", "perhaps", "put", "rather", "same", "say", "said", "see", "seen",
    "several", "shall", "she", "should", "since", "some", "something", "sometimes", "still",
    "such", "take", "taken", "than", "that", "the", "their", "them", "then", "there",
    "these", "they", "this", "those", "though", "through", "thus", "too", "under", "until",
    "upon", "use", "used", "using", "very", "was", "were", "what", "when", "where", "which",
    "while", "who", "whom", "whose", "why", "will", "with", "within", "without", "would",
    "year", "years", "yet", "your", "new", "well", "way", "work", "world", "would", "two",
    "three", "four", "five", "six", "seven", "eight", "nine", "ten", "half", "per", "cent",
    "percent", "million", "billion", "thousand", "hundred", "example", "examples", "show",
    "shows", "shown", "found", "find", "found", "become", "became", "include", "included",
    "including", "large", "small", "long", "high", "low", "good", "great", "little", "old",
    "young", "early", "late", "important", "different", "same", "local", "public", "human",
    "humans", "people", "person", "man", "men", "woman", "women", "child", "children",
    "group", "groups", "number", "numbers", "time", "times", "day", "days", "week", "month",
    "study", "studies", "research", "researchers", "scientists", "scientist", "evidence",
    "suggest", "suggests", "suggested", "believe", "believed", "think", "thought", "know",
    "known", "fact", "facts", "however", "therefore", "although", "though", "while",
    "passage", "paragraph", "paragraphs", "question", "questions", "answer", "answers",
    "reading", "following", "based", "below", "above", "section", "page", "pages",
    "minute", "minutes", "write", "written", "box", "boxes", "boxe", "word", "words",
    "statement", "statements", "choose", "chosen", "correct", "incorrect", "letter",
    "agree", "disagree", "true", "false", "heading", "headings", "list", "lists",
    "copyright", "compiled", "formatted", "proofread", "lightly", "commercial",
    "educational", "reproduced", "permission", "free", "help", "look", "walk",
    "today", "university", "college", "website", "email", "contact", "download",
    "according", "remain", "remains", "original", "complete", "completed", "result",
    "results", "problem", "problems", "idea", "ideas", "life", "place", "places",
    "right", "rights", "left", "help", "need", "needs", "want", "wanted", "look",
    "looking", "seem", "seems", "seemed", "become", "became", "begin", "began",
    "end", "ended", "start", "started", "continue", "continued", "set", "sets",
    "turn", "turns", "point", "points", "line", "lines", "part", "parts", "form",
    "forms", "type", "types", "kind", "kinds", "thing", "things", "lot", "lots",
    "bit", "way", "ways", "case", "cases", "hand", "hands", "side", "sides",
    "head", "heads", "body", "bodies", "home", "homes", "country", "countries",
    "city", "cities", "town", "towns", "land", "lands", "water", "waters", "air",
    "food", "foods", "book", "books", "paper", "papers", "report", "reports",
    "test", "tests", "course", "courses", "class", "classes", "school", "schools",
    "student", "students", "teacher", "teachers", "learn", "learned", "learning",
    "prohibited", "resale", "disclaimer", "endorsement", "affiliation", "publisher",
    "holder", "intact", "owner", "paid", "agre", "says", "said",
    "works", "work", "copy", "copies", "notice", "charge", "best", "better",
    "called", "underlying", "contradict", "contradicts", "lightly", "formatted",
    "proofread", "compiled", "reproduced", "permission", "commercial",
    "themselve", "themselves", "itself", "himself", "herself", "yourself",
    "didn", "doesn", "wasn", "isn", "haven", "hasn", "hadn", "won", "wouldn",
    "analysi", "processe", "wherea", "basi", "ourselve", "viii", "vii", "vi",
    "david", "william", "zealand",
}

# 雅思阅读高频学术词（种子 + 语料扩展）
SEED_WORDS = {
    "abandon", "ability", "able", "abnormal", "abolish", "abroad", "absence", "abstract",
    "abundant", "academic", "accelerate", "accept", "access", "accident", "accompany",
    "accomplish", "accord", "account", "accurate", "achieve", "acknowledge", "acquire",
    "adapt", "adequate", "adjacent", "adjust", "administration", "adopt", "adult",
    "advance", "advantage", "adverse", "advocate", "affect", "aggregate", "agriculture",
    "aid", "aim", "albeit", "allocate", "allow", "alter", "alternative", "ambiguous",
    "amenable", "analogy", "analyse", "analysis", "ancestor", "ancient", "angle",
    "annual", "anticipate", "apparent", "appeal", "appear", "application", "apply",
    "approach", "appropriate", "approximate", "arbitrary", "area", "argue", "argument",
    "arise", "artificial", "aspect", "assemble", "assess", "assign", "assist", "assume",
    "assumption", "attach", "attain", "attempt", "attitude", "attribute", "author",
    "authority", "available", "average", "aware", "behaviour", "behalf", "benefit",
    "bias", "bond", "brief", "bulk", "capable", "capacity", "category", "cease", "challenge",
    "channel", "characteristic", "chart", "chemical", "circumstance", "cite", "civil",
    "clarify", "classic", "clause", "code", "coherent", "coincide", "collapse", "colleague",
    "commence", "comment", "commission", "commit", "commodity", "communicate", "community",
    "compatible", "compensate", "compile", "complement", "complex", "component", "compound",
    "comprehensive", "comprise", "compute", "conceive", "concentrate", "concept", "conclude",
    "conclusion", "concurrent", "conduct", "confine", "confirm", "conflict", "conform",
    "consent", "consequent", "considerable", "consist", "constant", "constitute",
    "constraint", "construct", "consult", "consume", "contact", "contemporary", "context",
    "contract", "contradict", "contrary", "contrast", "contribute", "controversy",
    "convene", "conventional", "convert", "convince", "cooperate", "coordinate", "core",
    "corporate", "correspond", "couple", "create", "credit", "criteria", "crucial",
    "culture", "cumulative", "currency", "cycle", "data", "debate", "decade", "decline",
    "deduce", "define", "definite", "demonstrate", "denote", "dense", "deny", "depress",
    "derive", "design", "despite", "detect", "deviate", "device", "devote", "differentiate",
    "dimension", "diminish", "discrete", "discriminate", "displace", "display", "dispose",
    "distinct", "distort", "distribute", "diverse", "document", "domain", "domestic",
    "dominate", "draft", "drama", "duration", "dynamic", "economy", "edit", "element",
    "eliminate", "emerge", "emphasis", "empirical", "enable", "encounter", "energy",
    "enforce", "enhance", "enormous", "ensure", "entity", "environment", "equate",
    "equivalent", "error", "establish", "estimate", "ethic", "evaluate", "eventual",
    "evident", "evolve", "exceed", "exclude", "exhibit", "expand", "expert", "explicit",
    "exploit", "export", "expose", "external", "extract", "facilitate", "factor", "feature",
    "federal", "fee", "file", "final", "finance", "finite", "flexible", "fluctuate",
    "focus", "format", "formula", "forthcoming", "foundation", "framework", "function",
    "fundamental", "furthermore", "gender", "generate", "generation", "globe", "goal",
    "grade", "grant", "guarantee", "guideline", "hence", "hierarchy", "highlight",
    "hypothesis", "identical", "identify", "ideology", "ignorance", "illustrate", "image",
    "immigrate", "impact", "implement", "implicate", "implicit", "imply", "impose",
    "incentive", "incidence", "incline", "income", "incorporate", "index", "indicate",
    "individual", "induce", "inevitable", "infer", "infrastructure", "inherent", "inhibit",
    "initial", "initiate", "injure", "innovate", "input", "insert", "insight", "inspect",
    "instance", "institute", "instruct", "integral", "integrate", "integrity", "intelligence",
    "intense", "interact", "intermediate", "internal", "interpret", "interval", "intervene",
    "intrinsic", "invest", "investigate", "invoke", "involve", "isolate", "issue", "item",
    "job", "journal", "justify", "label", "layer", "lecture", "legal", "legislate",
    "levy", "liberal", "license", "likewise", "link", "locate", "logic", "maintain",
    "major", "manifest", "manual", "margin", "mature", "maximise", "mechanism", "media",
    "mediate", "medical", "medium", "mental", "method", "migrate", "military", "minimal",
    "minimum", "ministry", "minor", "mode", "modify", "monitor", "motive", "mutual",
    "negative", "network", "nevertheless", "nonetheless", "norm", "normal", "notion",
    "notwithstanding", "nuclear", "objective", "obtain", "obvious", "occupy", "occur",
    "odd", "offset", "ongoing", "option", "orient", "origin", "outcome", "output",
    "overall", "overlap", "overseas", "panel", "paradigm", "paragraph", "parallel",
    "parameter", "participate", "partner", "passive", "peak", "percent", "period",
    "persist", "perspective", "phase", "phenomenon", "philosophy", "physical", "plus",
    "policy", "portion", "pose", "positive", "potential", "practitioner", "precede",
    "precise", "predict", "predominant", "preliminary", "presume", "previous", "primary",
    "prime", "principal", "principle", "prior", "priority", "proceed", "process",
    "professional", "prohibit", "project", "promote", "proportion", "propose", "prospect",
    "protocol", "psychology", "publication", "publish", "purchase", "pursue", "qualify",
    "quote", "radical", "random", "range", "ratio", "rational", "react", "recover",
    "refine", "reflect", "reform", "regime", "region", "register", "regulate", "reject",
    "relate", "relax", "release", "relevant", "reliable", "rely", "remove", "require",
    "research", "resemble", "resolve", "resource", "respond", "restore", "restrain",
    "restrict", "retain", "reveal", "revenue", "reverse", "revise", "revolution",
    "rigid", "role", "route", "scenario", "schedule", "scheme", "scope", "section",
    "sector", "secure", "seek", "select", "sequence", "series", "shift", "significant",
    "similar", "simulate", "site", "so-called", "sole", "somewhat", "source", "specific",
    "specify", "sphere", "stable", "statistic", "status", "straightforward", "strategy",
    "stress", "structure", "style", "subject", "submit", "subsequent", "subsidy",
    "substitute", "successor", "sufficient", "sum", "summary", "supplement", "supply",
    "survey", "survive", "suspend", "sustain", "symbol", "symptom", "synthesis", "system",
    "target", "task", "team", "technical", "technique", "technology", "temporary",
    "tense", "terminate", "text", "theme", "theory", "thereby", "therefore", "thesis",
    "topic", "trace", "tradition", "transfer", "transform", "transit", "transmit",
    "transport", "trend", "trigger", "ultimate", "undergo", "underlie", "undertake",
    "uniform", "unique", "utilise", "valid", "variable", "vary", "vehicle", "version",
    "via", "violate", "virtual", "visible", "vision", "visual", "volume", "voluntary",
    "welfare", "whereas", "whereby", "widespread", "witness",
}

PHRASES: list[tuple[str, str, str]] = [
    (r"\baccording to\b", "according to", "据……所说；根据"),
    (r"\bin contrast\b", "in contrast", "相比之下（对比考点）"),
    (r"\bin contrast to\b", "in contrast to", "与……形成对比"),
    (r"\brather than\b", "rather than", "而非；不是……而是（偷换对象高频）"),
    (r"\binstead of\b", "instead of", "代替；而不是"),
    (r"\bas a result\b", "as a result", "因此；结果（因果）"),
    (r"\bas a result of\b", "as a result of", "由于；因为"),
    (r"\bdespite\b", "despite", "尽管（让步，易与因果混淆）"),
    (r"\bin spite of\b", "in spite of", "尽管"),
    (r"\bnot only\b.*\bbut also\b", "not only … but also", "不仅……而且……"),
    (r"\bin terms of\b", "in terms of", "就……而言；在……方面"),
    (r"\bwith respect to\b", "with respect to", "关于；就……而言"),
    (r"\bas opposed to\b", "as opposed to", "与……相反；而非"),
    (r"\bcompared with\b|\bcompared to\b", "compared with/to", "与……相比（比较考点）"),
    (r"\bin addition\b", "in addition", "此外；另外"),
    (r"\bfor instance\b|\bfor example\b", "for instance / for example", "例如（举例≠全部）"),
    (r"\bfar from\b", "far from", "远非；远未（否定强调）"),
    (r"\bthere is no doubt\b", "there is no doubt", "毫无疑问（绝对语气）"),
    (r"\bplay a .* role\b", "play a role in", "在……中起作用"),
    (r"\bbe attributed to\b", "be attributed to", "归因于（因果）"),
    (r"\bbe responsible for\b", "be responsible for", "对……负责；是……的原因"),
    (r"\bresult in\b", "result in", "导致（结果）"),
    (r"\bresult from\b", "result from", "源于（原因）"),
    (r"\blead to\b", "lead to", "导致"),
    (r"\bstem from\b", "stem from", "源于；来自"),
    (r"\bcontribute to\b", "contribute to", "促成；加剧；贡献于"),
    (r"\baccount for\b", "account for", "解释；占……比例"),
    (r"\brefer to\b", "refer to", "指；提及；查阅"),
    (r"\bconsist of\b", "consist of", "由……组成"),
    (r"\bcomprise\b", "comprise", "包含；由……组成"),
    (r"\bdepend on\b|\bdepend upon\b", "depend on", "取决于"),
    (r"\bregardless of\b", "regardless of", "不管；不顾"),
    (r"\bprovided that\b", "provided that", "假如；只要"),
    (r"\bas long as\b", "as long as", "只要"),
    (r"\bso that\b", "so that", "以便；所以"),
    (r"\bin order to\b", "in order to", "为了"),
    (r"\bthe majority of\b", "the majority of", "大多数（部分≠全部）"),
    (r"\ba number of\b", "a number of", "许多（数量模糊）"),
    (r"\ba variety of\b", "a variety of", "各种各样的"),
    (r"\bto some extent\b", "to some extent", "在某种程度上（程度限定）"),
    (r"\bby no means\b", "by no means", "绝不（否定绝对词）"),
    (r"\bno longer\b", "no longer", "不再（时间变化）"),
    (r"\bused to\b", "used to", "曾经（过去习惯/状态）"),
    (r"\bit is .* that\b", "It is … that …", "强调句（定位主干）"),
    (r"\bthe same .* as\b", "the same … as", "与……相同（比较）"),
    (r"\bmore .* than\b", "more … than", "比……更（比较级）"),
    (r"\bthe most\b", "the most", "最……（最高级）"),
    (r"\bnot until\b", "not until", "直到……才（否定+倒装）"),
    (r"\bonly when\b", "only when", "只有当……"),
    (r"\bwhether .* or\b", "whether … or", "是……还是；无论"),
]

PATTERN_STATS: list[tuple[str, str, str]] = [
    (r"\bhowever\b", "However, …", "转折：后文常才是作者真实观点"),
    (r"\bnevertheless\b|\bnonetheless\b", "Nevertheless / Nonetheless", "尽管如此（强转折）"),
    (r"\bwhereas\b", "…, whereas …", "对比：前后两项对照，填空/判断常考"),
    (r"\bwhile\b", "While …, …", "虽然/而；易与 when 混淆"),
    (r"\bunlike\b", "Unlike …, …", "与……不同（对比考点）"),
    (r"\bsimilar to\b", "similar to", "与……相似（勿与 same 等同）"),
    (r"\bmoreover\b|\bfurthermore\b", "Moreover / Furthermore", "递进：补充新信息"),
    (r"\bin fact\b|\bactually\b", "in fact / actually", "事实上（常修正前文）"),
    (r"\bon the contrary\b", "on the contrary", "相反（强反驳）"),
    (r"\bconversely\b", "conversely", "反过来"),
    (r"\balthough\b|\bthough\b", "Although / Though", "让步从句"),
    (r"\bdespite\b|\bin spite of\b", "Despite / In spite of", "Despite + 名词/动名词"),
    (r"\brather than\b", "rather than", "而非 X（选项偷换）"),
    (r"\bas opposed to\b", "as opposed to", "与……相对"),
    (r"\bthe reason .* is that\b", "The reason … is that", "原因句式"),
    (r"\bit appears that\b|\bit seems that\b", "It appears/seems that", "似乎（弱确定性→NG 信号）"),
    (r"\bthere is evidence that\b", "There is evidence that", "有证据表明"),
    (r"\bresearch suggests that\b", "Research suggests that", "研究表明（主观程度）"),
    (r"\bnot all\b", "not all", "并非全部（部分否定）"),
    (r"\b few\b|\b little\b", "few / little", "否定限定（数量）"),
]

ZH: dict[str, str] = {
    "abandon": "放弃；遗弃", "ability": "能力", "abstract": "抽象的", "abundant": "丰富的",
    "accelerate": "加速", "access": "获取；通道", "accompany": "伴随", "accomplish": "完成",
    "accurate": "准确的", "achieve": "实现", "acknowledge": "承认；致谢", "acquire": "获得",
    "adapt": "适应；改编", "adequate": "足够的", "adjust": "调整", "adopt": "采用；收养",
    "advance": "推进；前进", "advantage": "优势", "adverse": "不利的", "advocate": "倡导",
    "affect": "影响", "aggregate": "总计；集合", "agriculture": "农业", "allocate": "分配",
    "alter": "改变", "alternative": "替代的；选择", "ambiguous": "模糊的", "ancestor": "祖先",
    "ancient": "古代的", "annual": "年度的", "anticipate": "预期", "apparent": "明显的",
    "appeal": "吸引力；上诉", "application": "应用；申请", "approach": "方法；接近",
    "appropriate": "适当的", "approximate": "大约的", "arbitrary": "任意的", "argument": "论证；争论",
    "arise": "出现；产生", "artificial": "人工的", "aspect": "方面", "assess": "评估",
    "assume": "假定；承担", "assumption": "假设", "attribute": "归因于；特质", "authority": "权威；当局",
    "available": "可获得的", "behaviour": "行为", "benefit": "益处", "bias": "偏见",
    "capacity": "能力；容量", "category": "类别", "challenge": "挑战", "characteristic": "特征",
    "circumstance": "情况", "cite": "引用", "classic": "经典的", "collapse": "崩溃；倒塌",
    "colleague": "同事", "comment": "评论", "commission": "委员会；委托", "commit": "犯；承诺",
    "communicate": "交流", "community": "社区", "complex": "复杂的", "component": "组成部分",
    "comprehensive": "全面的", "comprise": "包含", "concept": "概念", "conclude": "得出结论",
    "conclusion": "结论", "conduct": "进行；行为", "confine": "限制", "confirm": "确认",
    "conflict": "冲突", "conform": "符合；遵从", "consequent": "随之发生的", "considerable": "相当大的",
    "consist": "由…组成", "constant": "持续的；恒定的", "constitute": "构成", "constraint": "限制",
    "construct": "建造；构建", "consume": "消耗", "contemporary": "当代的", "context": "语境；背景",
    "contradict": "矛盾", "contrary": "相反的", "contrast": "对比", "contribute": "贡献；促成",
    "controversy": "争议", "conventional": "传统的", "convert": "转换", "convince": "说服",
    "core": "核心", "corporate": "企业的", "correspond": "对应；通信", "create": "创造",
    "criteria": "标准", "crucial": "关键的", "culture": "文化", "decline": "下降；拒绝",
    "deduce": "推断", "define": "定义", "demonstrate": "证明；展示", "denote": "表示",
    "derive": "源于；推导", "despite": "尽管", "detect": "检测；发现", "deviate": "偏离",
    "device": "装置", "devote": "致力于", "dimension": "维度", "diminish": "减少",
    "distinct": " distinct；distinct 明显的", "distribute": "分布；分配", "diverse": "多样的",
    "domestic": "国内的；家养的", "dominate": "主导", "duration": "持续时间", "dynamic": "动态的",
    "economy": "经济", "eliminate": "消除", "emerge": "出现", "emphasis": "强调",
    "empirical": "实证的", "enable": "使能够", "encounter": "遭遇", "energy": "能量",
    "enhance": "增强", "enormous": "巨大的", "ensure": "确保", "environment": "环境",
    "equivalent": "等价的", "establish": "建立", "estimate": "估计", "evaluate": "评估",
    "evidence": "证据", "evident": "明显的", "evolve": "进化；演变", "exceed": "超过",
    "exclude": "排除", "exhibit": "展示；表现出", "expand": "扩大", "explicit": "明确的",
    "exploit": "开发；剥削", "export": "出口", "expose": "暴露", "external": "外部的",
    "extract": "提取；摘录", "facilitate": "促进", "factor": "因素", "feature": "特征",
    "fluctuate": "波动", "focus": "聚焦", "function": "功能；运行", "fundamental": "基本的",
    "generate": "产生", "generation": "一代；产生", "globe": "全球", "hypothesis": "假设",
    "identify": "识别；认定", "illustrate": "说明；插图", "impact": "影响", "implement": "实施",
    "imply": "暗示", "impose": "强加", "incentive": "激励", "incorporate": "纳入；合并",
    "indicate": "表明", "individual": "个人；个别的", "inevitable": "不可避免的",
    "infer": "推断", "inherent": "固有的", "initial": "最初的", "innovate": "创新",
    "insight": "洞察", "instance": "例子", "integrate": "整合", "intelligence": "智力",
    "interact": "互动", "internal": "内部的", "interpret": "解释；口译", "investigate": "调查",
    "involve": "涉及", "isolate": "隔离；孤立", "issue": "问题；发布", "justify": "证明正当",
    "maintain": "维持；主张", "mechanism": "机制", "method": "方法", "migrate": "迁移",
    "modify": "修改", "monitor": "监控", "motivate": "激励", "negative": "负面的；否定的",
    "nevertheless": "尽管如此", "notion": "观念", "objective": "目标；客观的", "obtain": "获得",
    "occupy": "占据", "occur": "发生", "outcome": "结果", "overall": "总体的",
    "phenomenon": "现象", "physical": "身体的；物理的", "policy": "政策", "potential": "潜在的；潜力",
    "predict": "预测", "previous": "先前的", "primary": "主要的", "principle": "原则",
    "procedure": "程序", "process": "过程；处理", "promote": "促进；推广", "proportion": "比例",
    "propose": "提议", "prospect": "前景", "psychology": "心理学", "publish": "出版",
    "pursue": "追求", "range": "范围", "react": "反应", "reflect": "反映；思考",
    "region": "地区", "regulate": "调节；监管", "reject": "拒绝", "relevant": "相关的",
    "rely": "依赖", "require": "需要", "research": "研究", "resemble": " resemble；类似",
    "resolve": "解决", "resource": "资源", "respond": "回应", "reveal": "揭示",
    "revolution": "革命", "role": "角色；作用", "scenario": "情景", "significant": "重要的；显著的",
    "similar": "相似的", "simulate": "模拟", "source": "来源", "specific": "具体的",
    "species": "物种", "strategy": "策略", "structure": "结构", "subject": "主题；科目；受试者",
    "subsequent": "随后的", "substitute": "替代", "sufficient": "足够的", "summary": "总结",
    "survey": "调查", "survive": "幸存", "sustain": "维持", "symbol": "象征",
    "symptom": "症状", "technique": "技术", "technology": "科技", "temporary": "临时的",
    "theory": "理论", "therefore": "因此", "tradition": "传统", "transfer": "转移",
    "transform": "转变", "trend": "趋势", "trigger": "触发", "undergo": "经历",
    "underlie": "构成…基础", "undertake": "承担；着手", "unique": "独特的", "valid": "有效的",
    "variable": "变量；可变的", "vary": "变化", "version": "版本", "via": "经由",
    "visible": "可见的", "widespread": "广泛的", "witness": "见证",
    "author": "作者", "area": "区域；领域", "system": "系统；体系", "able": "能够的",
    "period": "时期；阶段", "major": "主要的；专业", "appear": "出现；似乎", "present": "当前的；呈现",
    "team": "团队", "popular": "流行的", "allow": "允许；使可能", "design": "设计",
    "project": "项目", "expert": "专家", "data": "数据", "environment": "环境",
    "complex": "复杂的", "create": "创造", "significant": "重要的；显著的", "role": "角色；作用",
    "theory": "理论", "technology": "科技", "impact": "影响", "region": "地区",
    "factor": "因素", "method": "方法", "range": "范围", "similar": "相似的",
    "despite": "尽管", "subject": "主题；科目", "individual": "个人；个别的", "process": "过程；处理",
        "develop": "发展；开发；患病",
        "themselves": "他们自己；本身",
        "themselve": "他们自己；本身",
        "developed": "发达的；已发展的",
        "produced": "生产的；产出的",
        "involved": "涉及的；复杂的",
        "experience": "经验；经历 | 体验",
        "impossible": "不可能的",
        "living": "生活的；活着的",
        "actually": "实际上；事实上",
        "particularly": "尤其；特别",
        "throughout": "贯穿；遍及",
        "variety": "多样性；种类",
        "strong": "强壮的；强烈的",
        "instead": "反而；代替",
        "along": "沿着；一起",
        "ever": "曾经；永远",
        "simply": "仅仅；简单地",
        "longer": "更长的；更久的",
        "nature": "自然；本性",
        "took": "take 过去式；拿；花费",
        "state": "状态；国家 | 陈述",
        "whether": "是否；无论…还是",
        "called": "被称为；叫做",
        "works": "作品；运作（work 三单）",
        "copy": "复制；副本",
        "notice": "注意到 | 通知；告示",
        "charge": "收费；指控 | 负责",
        "best": "最好的；最好地",
        "better": "更好的；较好",
        "distribution": "分布；分配；发行",
        "underlying": "潜在的；根本的",
        "possible": "可能的",
        "effect": "效果；影响",
        "century": "世纪",
        "writer": "作家",
        "order": "顺序；命令 | 订购",
        "animal": "动物",
        "certain": "某些；确定的",
        "common": "常见的；共同的",
        "particular": "特定的；特别的",
        "social": "社会的；社交的",
        "modern": "现代的",
        "development": "发展；开发",
        "together": "一起；共同",
        "live": "生活；居住 | 现场的",
        "second": "第二 | 秒",
        "recent": "最近的",
        "natural": "自然的；天然的",
        "view": "观点；视野 | 看待",
        "provide": "提供；规定",
        "almost": "几乎",
        "clear": "清楚的 | 清除",
        "history": "历史",
        "difficult": "困难的",
        "light": "光线；轻的",
        "call": "称呼；呼吁",
        "produce": "生产；产生",
        "understand": "理解",
        "interest": "兴趣；利益",
        "involve": "涉及；包含",
        "create": "创造；造成",
        "general": "总体的；一般的",
        "consider": "考虑；认为",
        "play": "扮演；发挥作用 | 玩耍",
        "match": "匹配；比赛",
        "support": "支持；支撑",
        "lead": "导致；引领",
        "cause": "原因 | 导致",
        "explain": "解释",
        "claim": "声称；主张",
        "discover": "发现",
        "require": "需要；要求",
        "note": "注意到 | 笔记",
        "grow": "生长；增长",
        "enough": "足够的",
        "actual": "实际的",
        "past": "过去的 | 过去",
        "increase": "增加",
        "main": "主要的",
        "skill": "技能",
        "condition": "条件；状况",
        "record": "记录 | 唱片",
        "near": "接近；附近",
        "likely": "可能的",
        "scientist": "科学家",
        "information": "信息；资料",
        "author": "作者",
        "available": "可获得的",
        "change": "改变；变化",
        "area": "区域；领域",
        "level": "水平；等级",
        "system": "系统；体系",
        "reason": "原因；理由",
        "similar": "相似的",
        "able": "能够的",
        "process": "过程；处理",
        "range": "范围",
        "ability": "能力",
        "period": "时期；阶段",
}

# 语料高频但 ZH/EXTRA 未覆盖的学术核心词
SEED_GAP_ZH: dict[str, str] = {
    "reference": "参考；提及", "science": "科学", "field": "领域；田野", "move": "移动；搬家",
    "ones": "人们（one 的复数）", "importance": "重要性", "matter": "事情；物质 | 要紧",
    "hard": "困难的；硬的", "south": "南方", "real": "真实的", "face": "脸 | 面对",
    "response": "回应", "outside": "在外面；外部", "demand": "需求 | 要求",
    "task": "任务", "third": "第三", "sentence": "句子", "north": "北方",
    "argue": "争论；主张", "series": "系列", "average": "平均的 | 平均",
    "supply": "供应", "institute": "研究所 | 建立", "professional": "专业的；专业人士",
    "whereas": "然而；鉴于", "academic": "学术的", "style": "风格", "visual": "视觉的",
    "apply": "申请；应用", "aware": "意识到的", "capable": "有能力的", "display": "展示",
    "furthermore": "此外", "shift": "转变；轮班", "precise": "精确的", "media": "媒体",
    "cycle": "循环", "assist": "协助", "journal": "期刊", "relate": "关联；叙述",
    "code": "代码；准则", "channel": "渠道", "release": "释放；发布", "route": "路线",
    "trace": "追踪；痕迹", "highlight": "强调；亮点", "prior": "先前的", "transport": "运输",
    "compound": "化合物；复合的", "gender": "性别", "medium": "媒介；中等的",
    "reliable": "可靠的", "retain": "保留", "couple": "一对；几个", "legal": "法律的",
    "emphasis": "强调", "philosophy": "哲学", "intense": "强烈的", "perspective": "视角",
    "priority": "优先", "sphere": "领域；球体", "purchase": "购买", "random": "随机的",
    "publication": "出版；出版物", "sector": "部门", "flexible": "灵活的", "minimum": "最小的",
    "somewhat": "有点", "identical": "相同的", "rational": "理性的", "select": "选择",
    "hence": "因此", "hypothesis": "假设", "sequence": "序列", "concentrate": "集中；浓缩",
    "dense": "密集的", "guarantee": "保证", "thereby": "从而", "prime": "主要的；首要的",
    "ultimate": "最终的", "drama": "戏剧", "plus": "加；优势", "uniform": "统一的；制服",
    "logic": "逻辑", "virtual": "虚拟的", "input": "输入", "grade": "等级；年级",
    "framework": "框架", "manual": "手册；手工的", "minimal": "最小的", "panel": "面板；专家组",
    "stable": "稳定的", "mature": "成熟的", "overseas": "海外的", "principal": "主要的；校长",
    "scope": "范围", "straightforward": "直接的", "output": "产出", "reverse": "逆转；反面",
    "schedule": "日程", "revenue": "收入", "guideline": "指南", "locate": "定位",
    "sole": "唯一的", "ongoing": "持续的", "persist": "持续；坚持", "portion": "部分",
    "nonetheless": "尽管如此", "practitioner": "从业者", "norm": "规范", "analyse": "分析",
    "mode": "模式", "civil": "公民的；民用的", "infrastructure": "基础设施", "deny": "否认",
    "hierarchy": "等级制度", "integral": "不可或缺的", "interval": "间隔", "likewise": "同样地",
    "peak": "峰值", "proceed": "进行", "restore": "恢复", "bond": "纽带；债券",
    "commodity": "商品", "definite": "明确的", "recover": "恢复", "supplement": "补充",
    "angle": "角度", "attach": "附上", "federal": "联邦的", "predominant": "占主导的",
    "secure": "安全的；获得", "photosynthesis": "光合作用", "formula": "公式",
    "ministry": "部委", "ratio": "比率", "induce": "诱导", "offset": "抵消",
    "finance": "金融 | 资助", "orient": "使朝向", "pose": "造成；摆姿势", "abroad": "在国外",
    "eventual": "最终的", "format": "格式", "initiate": "发起", "intrinsic": "内在的",
    "restrict": "限制", "specify": "明确规定", "thesis": "论文", "welfare": "福利",
    "incidence": "发生率", "quote": "引用", "attain": "达到", "synthesis": "综合",
    "accord": "一致 | 给予", "behalf": "代表", "bulk": "大部分", "clarify": "澄清",
    "contract": "合同 | 收缩", "intermediate": "中间的", "margin": "边缘；利润",
    "maximise": "最大化", "reform": "改革", "register": "登记", "relax": "放松",
    "subsidy": "补贴",
}


def load_yasi_dict() -> dict[str, str]:
    out: dict[str, str] = {}
    skip = ("考频", "例句", "ZYZ", "ZXZ")
    for p in sorted(ROOT.glob("content/posts/Yasi*.md")):
        if any(s in p.name for s in skip):
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^####\s+(.+)$", line.strip())
            if not m:
                continue
            body = m.group(1).strip()
            term, zh = body, ""
            for sep in ("：", ":"):
                if sep in body:
                    term, zh = body.split(sep, 1)
                    break
            term = re.sub(r"\*\*", "", term.strip()).lower()
            zh = re.sub(r"\*\*", "", zh.strip())
            if term and zh and " " not in term:
                out[term] = zh
    return out


def lemma_simple(w: str) -> str:
    wl = w.lower()
    if wl in IRREGULAR:
        return IRREGULAR[wl]
    if wl in PLURAL_KEEP:
        return wl
    if wl.endswith("ies") and len(wl) > 4:
        return wl[:-3] + "y"
    if wl.endswith("s") and len(wl) > 4 and not wl.endswith("ss") and not wl.endswith("us"):
        return wl[:-1]
    return wl


def load_zh_cache() -> dict[str, str]:
    if ZH_CACHE.is_file():
        return json.loads(ZH_CACHE.read_text(encoding="utf-8"))
    return {}


def save_zh_cache(cache: dict[str, str]) -> None:
    ZH_CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=0), encoding="utf-8")


def google_translate(text: str) -> str:
    import urllib.parse
    import urllib.request

    q = text[:400]
    url = (
        "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t&q="
        + urllib.parse.quote(q)
    )
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = json.loads(r.read().decode())
    parts = [x[0] for x in data[0] if x[0]]
    return "".join(parts).strip()


def fetch_dict_defs(word: str) -> list[str]:
    import urllib.parse
    import urllib.request

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{urllib.parse.quote(word)}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read().decode())
    except Exception:
        return []
    defs: list[str] = []
    for entry in data[:1]:
        for m in entry.get("meanings", [])[:3]:
            pos = m.get("partOfSpeech", "")
            for d in m.get("definitions", [])[:2]:
                t = d.get("definition", "").strip()
                if t:
                    prefix = f"{pos}. " if pos else ""
                    defs.append(prefix + t[:120])
    return defs[:4]


def build_meaning(word: str, yasi: dict[str, str], cache: dict[str, str], use_api: bool = False) -> str:
    w = word.lower()
    static = {**SEED_GAP_ZH, **EXTRA_ZH, **ZH}
    keys = [w, lemma_simple(w)]
    if w.endswith("ed") and len(w) > 5:
        keys += [w[:-2], w[:-1]]
    if w.endswith("ing") and len(w) > 6:
        keys += [w[:-3], w[:-3] + "e"]
    if w.endswith("ly") and len(w) > 5:
        keys += [w[:-2]]
    for k in keys:
        if k in yasi:
            return yasi[k]
        if k in static:
            return static[k]
    cached = cache.get(w, "")
    if cached and "待补" not in cached and not cached.startswith("名词。"):
        return cached
    if not use_api:
        return ""
    defs = fetch_dict_defs(w)
    if not defs:
        return ""
    gloss = " | ".join(d.split(". ", 1)[-1] if ". " in d else d for d in defs)
    try:
        zh = google_translate(gloss)
        zh = re.sub(r"\s+", " ", zh).strip()
        out = zh if zh else gloss
    except Exception:
        out = gloss
    cache[w] = out
    time.sleep(0.1)
    return out


def count_corpus_words(corpus: list[dict]) -> tuple[dict[str, set[str]], Counter[str]]:
    word_docs: dict[str, set[str]] = defaultdict(set)
    word_total: Counter[str] = Counter()
    for item in corpus:
        seen: set[str] = set()
        for tok in re.findall(r"[a-z]{4,}", item["text_lower"]):
            if not is_valid_word(tok):
                continue
            lem = lemma_simple(tok)
            if not is_valid_word(lem):
                continue
            word_total[lem] += 1
            if lem not in seen:
                seen.add(lem)
                word_docs[lem].add(item["file"])
    return word_docs, word_total


def select_word_entries(
    corpus: list[dict],
    word_docs: dict[str, set[str]],
    word_total: Counter[str],
    yasi: dict[str, str],
    min_words: int = MIN_WORDS,
) -> list[dict]:
    ranked = sorted(word_docs.items(), key=lambda x: (-len(x[1]), -word_total[x[0]]))
    chosen: dict[str, dict] = {}

    def add(w: str, priority: int = 0) -> None:
        lem = lemma_simple(w)
        if lem in STOP or len(lem) < 4:
            return
        dc = len(word_docs.get(lem, set()))
        if dc < 3:
            return
        if lem not in chosen or chosen[lem]["doc_count"] < dc:
            chosen[lem] = {
                "term": lem,
                "doc_count": dc,
                "total": word_total.get(lem, 0),
                "priority": priority,
            }

    for w in SEED_WORDS:
        add(w, 2)
    for w in yasi:
        add(w, 3)

    for lem, files in ranked:
        if lem in chosen:
            continue
        if len(lem) < 4 or lem in STOP or len(files) < 12:
            continue
        chosen[lem] = {
            "term": lem,
            "doc_count": len(files),
            "total": word_total.get(lem, 0),
            "priority": 0,
        }
        if len(chosen) >= min_words:
            break

    entries = sorted(
        chosen.values(),
        key=lambda x: (-x["doc_count"], -x["priority"], -x["total"], x["term"]),
    )
    return entries[:min_words]


def load_yasi_terms() -> set[str]:
    return set(load_yasi_dict().keys())


def clean_text(text: str) -> str:
    text = EXAM_NOISE.sub(" ", text)
    # 去掉页眉页脚常见水印块
    text = re.sub(r"\b\d+\s+minutes?\b", " ", text, flags=re.I)
    text = re.sub(r"\b(write|choose|complete)\b[^.]{0,40}\b(box(es)?|answer(s)?)\b", " ", text, flags=re.I)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def is_valid_word(w: str) -> bool:
    if w in STOP or len(w) < 4:
        return False
    if w.endswith("ed") and w[:-2] in STOP:
        return False
    if w.endswith("ing") and w[:-3] in STOP:
        return False
    if w.endswith("ly") and w[:-2] in STOP:
        return False
    return True


def base_form(w: str) -> str:
    return lemma_simple(w)


def load_corpus(use_cache: bool = True) -> list[dict]:
    if use_cache and CACHE.is_file():
        data = json.loads(CACHE.read_text(encoding="utf-8"))
        return data
    if not PDF_DIR.is_dir():
        print(f"PDF 目录不存在: {PDF_DIR}", file=sys.stderr)
        sys.exit(1)
    corpus: list[dict] = []
    for pdf in sorted(PDF_DIR.glob("*.pdf")):
        doc = fitz.open(pdf)
        raw = " ".join(page.get_text() for page in doc)
        doc.close()
        text = clean_text(raw)
        corpus.append({"file": pdf.name, "text": text, "text_lower": text.lower()})
    CACHE.write_text(json.dumps(corpus, ensure_ascii=False), encoding="utf-8")
    print(f"[cache] 已缓存 {len(corpus)} 篇 → {CACHE}")
    return corpus


def word_in_text(word: str, text: str) -> bool:
    return bool(re.search(rf"\b{re.escape(word)}\b", text, re.I))


def find_example(word: str, corpus: list[dict], max_len: int = 280) -> tuple[str, str] | None:
    pat = re.compile(rf"\b{re.escape(word)}\b", re.I)
    for item in corpus:
        for sent in SENT_SPLIT.split(item["text"]):
            s = sent.strip()
            if len(s) < 40 or len(s) > max_len or not pat.search(s):
                continue
            if EXAM_NOISE.search(s):
                continue
            short = re.sub(r"\s+", " ", s)
            return item["file"][:40], short
    return None


def tier(n: int, total: int) -> str:
    if n >= 80:
        return "S"
    if n >= 40:
        return "A"
    if n >= 15:
        return "B"
    if n >= 8:
        return "C"
    return "D"


def zh_word(w: str, yasi: dict[str, str], cache: dict[str, str]) -> str:
    g = build_meaning(w, yasi, cache, False)
    return g if g else "（待补）"


def main() -> None:
    corpus = load_corpus(use_cache=CACHE.is_file())
    total = len(corpus)
    print(f"[zyz] 语料 {total} 篇")

    yasi = load_yasi_dict()
    zh_cache = load_zh_cache()
    word_docs, word_total = count_corpus_words(corpus)
    entries = select_word_entries(corpus, word_docs, word_total, yasi, MIN_WORDS)
    print(f"[zyz] 选定 {len(entries)} 词")

    # 离线释义覆盖率
    for e in entries:
        build_meaning(e["term"], yasi, zh_cache, use_api=False)

    missing = [e["term"] for e in entries if not build_meaning(e["term"], yasi, zh_cache, False)]
    if "--online" in sys.argv and missing:
        cap = int(sys.argv[sys.argv.index("--online") + 1]) if len(sys.argv) > sys.argv.index("--online") + 1 and sys.argv[sys.argv.index("--online") + 1].isdigit() else 80
        print(f"[zyz] 在线补全最多 {cap} 词（剩余 {len(missing)}）…")
        for i, w in enumerate(missing[:cap]):
            build_meaning(w, yasi, zh_cache, use_api=True)
            if (i + 1) % 20 == 0:
                save_zh_cache(zh_cache)
        save_zh_cache(zh_cache)
    else:
        print(f"[zyz] 离线模式：{len(missing)} 词暂无释义（可加 --online 80 分批补全）")

    def gloss(term: str) -> str:
        g = build_meaning(term, yasi, zh_cache, False)
        if g:
            return g.replace("|", "；")
        return "（待补）"

    def gloss_short(term: str, n: int = 36) -> str:
        return gloss(term)[:n]

    # 短语统计
    phrase_entries: list[dict] = []
    for pat, label, zh in PHRASES:
        docs: set[str] = set()
        example = None
        for item in corpus:
            if re.search(pat, item["text_lower"]):
                docs.add(item["file"])
                if not example:
                    for sent in SENT_SPLIT.split(item["text"]):
                        if re.search(pat, sent, re.I) and 40 < len(sent) < 300:
                            example = (item["file"][:35], re.sub(r"\s+", " ", sent.strip()))
                            break
        if docs:
            phrase_entries.append({
                "term": label, "doc_count": len(docs), "zh": zh, "example": example, "type": "phrase",
            })
    phrase_entries.sort(key=lambda x: -x["doc_count"])

    # 句式统计
    pattern_entries: list[dict] = []
    for pat, label, note in PATTERN_STATS:
        docs: set[str] = set()
        ex = None
        for item in corpus:
            if re.search(pat, item["text_lower"]):
                docs.add(item["file"])
                if not ex:
                    for sent in SENT_SPLIT.split(item["text"]):
                        if re.search(pat, sent, re.I) and 30 < len(sent) < 280:
                            ex = re.sub(r"\s+", " ", sent.strip())
                            break
        if docs:
            pattern_entries.append({"label": label, "doc_count": len(docs), "note": note, "example": ex})
    pattern_entries.sort(key=lambda x: -x["doc_count"])

    lines = [
        "---",
        "title: Yasi-ZYZ 阅读考频",
        "date: 2026-05-22",
        "tags: 学习/雅思",
        "column: 学习笔记",
        "toc: true",
        "---",
        "",
        "# Yasi-ZYZ 雅思阅读 · 考频总表",
        "",
        f"> **语料**：`e:/BaiduNetdiskDownload/ZYZ/PDF` 共 **{total}** 篇阅读真题/练习 PDF。",
        f"> **词条**：收录 **{len(entries)}** 个高频词 + **{len(phrase_entries)}** 个高频短语（释义含 Yasi 笔记 + 语料义项）。",
        "> **排序**：先按 **出现篇数** 降序，再按 **总出现次数** 降序。",
        "",
        "## 考频分级",
        "",
        "| 级别 | 出现篇数 | 建议 |",
        "|------|----------|------|",
        f"| **S** | ≥80 篇 | 几乎每套必见，优先背 |",
        f"| **A** | 40–79 篇 | 高频考点词 |",
        "| **B** | 15–39 篇 | 重点复习 |",
        "| **C** | 8–14 篇 | 认识即可 |",
        "| **D** | 3–7 篇 | 本语料偶见 |",
        "",
        "## 速览 Top 50 词",
        "",
        "| 词 | 中文 | 篇数 | 次数 | 级别 |",
        "|----|------|------|------|------|",
    ]
    for e in entries[:50]:
        t = tier(e["doc_count"], total)
        lines.append(
            f"| {e['term']} | {gloss_short(e['term'])} | {e['doc_count']} | {e['total']} | {t} |"
        )

    lines += [
        "",
        "## 速览 Top 25 短语",
        "",
        "| 短语 | 中文 | 篇数 | 阅读注意 |",
        "|------|------|------|----------|",
    ]
    for p in phrase_entries[:25]:
        lines.append(f"| {p['term']} | {p['zh']} | {p['doc_count']} | 见下节「常见坑」 |")

    # 阅读常见坑
    lines += [
        "",
        "## 阅读常见坑（结合 ZYZ 语料）",
        "",
        "### 1. FALSE vs NOT GIVEN",
        "",
        "| 类型 | 信号 | 处理 |",
        "|------|------|------|",
        "| **FALSE** | 题干与原文**直接矛盾**（反义、数字错、对象错） | 原文能**明确反驳**题干 |",
        "| **NOT GIVEN** | 原文**未提及**或**无法推断** | 原文没说过 / 证据不足 |",
        "",
        "> **坑**：把「原文没写」当成 FALSE；或把「自己推理」当成原文说了。",
        "",
        "### 2. 绝对词 & 程度词（NG/FALSE 高发）",
        "",
        "| 词 | 风险 |",
        "|----|------|",
        "| all / every / always / never / only / must | 题干含绝对词 → 原文常有限定 → 易 FALSE |",
        "| some / may / might / often / tend to / suggest | 原文弱表述 → 题干改肯定 → 易 FALSE/NG |",
        "| the majority / mainly / largely | 部分≠全部；「大多数」≠「所有」 |",
        "",
        "### 3. 偷换对象（rather than / instead of）",
        "",
        f"> 语料命中 **{next((p['doc_count'] for p in phrase_entries if p['term']=='rather than'), 0)}** 篇含 **rather than**，**{next((p['doc_count'] for p in phrase_entries if p['term']=='instead of'), 0)}** 篇含 **instead of**。",
        "> 题干常把「A rather than B」改成「B rather than A」，或把比较对象换成近义词。",
        "",
        "### 4. 对比 & 转折（However / Unlike / Whereas）",
        "",
        f"> **However** 出现于 **{next((x['doc_count'] for x in pattern_entries if 'However' in x['label']), 0)}** 篇；**Unlike** 短语 **{next((p['doc_count'] for p in phrase_entries if 'compared' in p['term']), 0)}** 篇含 compared with/to。",
        "> 转折后才是重点；判断题考「转折前信息」常为 FALSE。",
        "",
        "### 5. 因果倒置（result in / result from / lead to）",
        "",
        "> **result in** = 导致（结果）；**result from** = 源于（原因）。题干互换因果 → FALSE。",
        "",
        "### 6. 部分正确陷阱",
        "",
        "> 选项一半对、一半错 → 整体 FALSE；填空题同义替换勿接受「沾边义」。",
        "",
        "### 7. 举例 ≠ 结论（for example / for instance）",
        "",
        f"> 语料 **{next((p['doc_count'] for p in phrase_entries if 'for instance' in p['term']), 0)}** 篇含 for example/instance。举例仅说明一点，不能推广为作者全部观点。",
        "",
        "### 8. 时间 / 频率变化（used to / no longer / until）",
        "",
        "> 原文「曾经…现在不」→ 题干说「一直…」= FALSE；**not until** 倒装句先抓时间逻辑。",
        "",
        "## 常见句式（语料统计 + 阅读要点）",
        "",
        "| 句式 | 篇数 | 阅读要点 | 例句（摘自语料） |",
        "|------|------|----------|------------------|",
    ]
    for p in pattern_entries[:22]:
        ex = (p.get("example") or "—")[:120]
        if len(ex) > 117:
            ex = ex[:117] + "…"
        lines.append(f"| {p['label']} | {p['doc_count']} | {p['note']} | {ex} |")

    lines += ["", "## 按考频展开 · 词汇（全表）", ""]

    current = None
    for e in entries:
        t = tier(e["doc_count"], total)
        if t != current:
            current = t
            labels = {
                "S": "S级·≥80篇",
                "A": "A级·40–79篇",
                "B": "B级·15–39篇",
                "C": "C级·8–14篇",
                "D": "D级·3–7篇",
            }
            lines += ["", f"### {labels[t]}", ""]
        zh = gloss(e["term"])
        lines.append(f"#### {e['term']}：{zh}")
        lines.append("")
        lines.append(f"> **{e['doc_count']}** 篇 / **{e['total']}** 次 · 级别 **{t}**")
        if t in ("S", "A") and e["doc_count"] >= 40:
            ex = find_example(e["term"], corpus)
            if ex:
                lines.append(f"> 例：**{ex[0]}** — {ex[1]}")
        lines.append("")

    # 删除旧的 B/C/D 紧凑表（已并入全表）

    lines += ["", "## 按考频展开 · 短语", ""]
    for p in phrase_entries:
        t = tier(p["doc_count"], total)
        lines.append(f"#### {p['term']}：{p['zh']}")
        lines.append("")
        lines.append(f"> **{p['doc_count']}** 篇 · 级别 **{t}**")
        if p.get("example"):
            lines.append(f"> 例：**{p['example'][0]}** — {p['example'][1]}")
        lines.append("")

    lines += [
        "",
        "---",
        "",
        "## 说明",
        "",
        "- 语料路径：`e:/BaiduNetdiskDownload/ZYZ/PDF`（ZYZ 阅读 PDF 全集）。",
        "- 词频按**出现篇数**统计（同一 PDF 只计 1 次），比纯词频更接近「考频」。",
        "- 可与 [`Yasi.md`](Yasi.md) 个人生词本、[`Yasi-ZXZ-阅读例句.md`](Yasi-ZXZ-阅读例句.md) 对照使用。",
        "- 释义优先 [`Yasi.md`](Yasi.md) 个人笔记；其余为雅思阅读义项 + 在线词典补充。",
        "- 重新生成：`python web/scripts/build-yasi-zyz-reading-freq-md.py`",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"[zyz] → {OUT}")
    s = sum(1 for e in entries if tier(e["doc_count"], total) == "S")
    a = sum(1 for e in entries if tier(e["doc_count"], total) == "A")
    print(f"  词 {len(entries)}，短语 {len(phrase_entries)}，S级 {s}，A级 {a}")


if __name__ == "__main__":
    main()
