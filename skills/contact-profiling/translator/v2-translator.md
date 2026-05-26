# V2.0 Translator Module

> Contact Profiling V2.0 翻译模块(Phase 1 骨架版)
> 作者: Munkh & Kiro
> 起草: 2026-05-17
> 状态: 🟡 骨架版,Phase 2 用 Hermes 内容 + V2.0 references 填充细化

---

## 这个文件是什么

**Translator 模块是 Contact Profiling 给所有下游 Skill 的对外接口**:

输入:Record 文件中的内部框架标签字段
输出:按目的(purpose)翻译后的大白话措辞
保证:输入字段名 + 输出语义在 V2.0 周期内稳定

**谁用这个模块?**
- ✅ Contact Profiling 自己的 View 层(渲染 HTML/PDF 时)
- ✅ Simulator V2.0(扮演时理解原始标签)
- ✅ 未来其他 Skill 在升级到模式 B 时
- ❌ 不是给 User 看的,User 拿到的永远是这个模块翻译后的产物

---

## 接口契约(LOCKED)

### 输入字段表

| 字段名 | 来源 | 取值范围 |
|---|---|---|
| `maslow_active_level` | maslow-tob.md | 安全 / 尊重 / 自我实现 / null |
| `disc_label` | disc.md | D / I / S / C / D-I / D-C / I-S / S-C / null |
| `disc_label.default_vs_displayed` | disc.md | default / displayed / mixed / unknown |
| `cognitive_function_stack` | mbti.md | Ne-Ti / Ni-Te / Te-Ni / Si-Fe / Se-Fe / ... / null(以 V2.0 references 重构后清单为准) |
| `preferred_attention` | mbti.md (投影) | S / N / null |
| `preferred_judgment` | mbti.md (投影) | T / F / null |
| `enneagram_motivation` | enneagram.md | 1-9 / null(只用动机面) |
| `fear_pattern.outer` | fear-three-rings.md | 字符串描述 / null |
| `fear_pattern.middle` | fear-three-rings.md | 字符串描述 / null |
| `fear_pattern.inner` | fear-three-rings.md | 字符串描述 / null |
| `trust_stage` | trust-frameworks.md | 陌生供应商 / 可以合作的一家 / 能帮他解决问题的人 / 他愿意听意见的顾问 / 深度绑定的伙伴 |
| `pressure_signals` | stress-detection.md | array,每条带 signal/trigger_context |
| `china_signals` | china-calibration.md | array,每条带 signal/interpretation |
| `aspiration_signals` | SKILL.md | array,每条带 signal |
| `aspiration_status` | SKILL.md | to_explore / tentatively_understood / confirmed |
| `mission_indicators.triggered` | SKILL.md | boolean |

### 支持的 purpose

```
overview              — 总览(默认),完整 V1.6 形式
pre-visit             — 拜访准备,重点是怎么配合 + 别踩雷
ebc-prep              — EBC 准备,重点是公司战略对齐 + 沟通偏好
relationship-review   — 关系复盘,重点是当前关系阶段 + 推进方向
objection-handling    — 异议应对,重点是回避模式
custom                — User 自由描述,LLM 解释后映射到上述某个 purpose 或独立装配
simulator-roleplay    — Simulator V2.0 用(Phase 2 加,V2.0 阶段 1 暂用 pre-visit 兜底)
bttroc-archetype-hint — BTTROC 用,从 V2.0 字段推 5 archetype 倾向 hint(不下结论)
                        ↑ V2.0 update 2 新增 (2026-05-20)
```

> **未来扩展**:其他 skill 需要专属翻译时,在这清单加新 purpose + 在下方"翻译规则"部分加对应字段 × 新 purpose 的措辞。**新 purpose 不破坏 V2.0 字段名 / 输出语义 LOCKED 承诺**(R14.3 / R14.4),只扩展不收缩。

### 输出语义稳定承诺(R14.4)

我承诺以下"语义"在 V2.0 周期内稳定 — 具体措辞可迭代,但**含义不漂移**:

| 输入 | 输出语义不变量 |
|---|---|
| `disc_label = D` | 做决定直接、要结论、节奏快 |
| `disc_label = I` | 重交流、爱讲故事、需要被认同 |
| `disc_label = S` | 温和、不急、怕变化、不直接说不 |
| `disc_label = C` | 要数据、要逻辑、追求完美 |
| `cognitive_function_stack = Ne-Ti` | 探索新可能性 + 内在逻辑校验 |
| `cognitive_function_stack = Te-Ni` | 直接看效率 + 自带方向感 |
| `cognitive_function_stack = Si-Fe` | 靠经验做判断 + 关心团队和谐 |
| `enneagram_motivation = 1` | 怕犯错,追求完美 |
| `enneagram_motivation = 3` | 追求成功 + 被认可 |
| `enneagram_motivation = 6` | 怕不安全 + 重忠诚 |
| `enneagram_motivation = 8` | 追求掌控 + 不被控制 |
| `trust_stage = 陌生供应商` | 关系第 1 阶段,他在评估"你是谁" |
| `trust_stage = 顾问` | 关系深度阶段,他主动征询意见 |

(Phase 2 完整化后,每个字段每个取值的语义不变量都列在这里)

---

## 翻译规则(按字段 × 目的)

> **Phase 1 骨架版仅给关键字段 × 关键 purpose 的措辞。**
> Phase 2 用 Hermes 培训文档内容 + V2.0 references 重构结果填充完整。

### 字段:disc_label

#### purpose: overview

| 取值 | 大白话(用在 View 总览版 + Record V1.6 兼容章节) |
|---|---|
| D | "他做决定时直接,要看结论,不爱铺垫" |
| I | "他喜欢从交流里来回找感觉,讲故事让他更投入" |
| S | "他需要时间消化,不喜欢被追节奏,关系比单子重要" |
| C | "他要细节,要标准,要逻辑闭环,数据不全的话他不会前进" |
| D-I | "他做事直接,但喜欢通过聊天找感觉,先讲结论再聊原因" |
| D-C | "他要结论,但结论必须有数据支撑,不接受'差不多'" |
| I-S | "他爱聊天但不爱催,关系第一,业务推进他会客气拒绝" |
| S-C | "他温和但要细节,看似配合实际有自己的标准,慢但扎实" |

#### purpose: pre-visit

| 取值 | 给 User 的拜访准备建议 |
|---|---|
| D | "建议你先放结论,3 句以内进入主题。准备 1 个 takeaway 在他打断前讲完" |
| I | "开场可以多 1-2 句寒暄,谈案例比谈数据更打动他" |
| S | "节奏放慢,别赶,允许他询问背景,展示你的稳定性" |
| C | "材料要全,数据有口径标注,问题有 backup 答案" |

#### purpose: ebc-prep

| 取值 | EBC 准备建议 |
|---|---|
| D | "EBC 内容前 30 秒进结论。避免长背景铺垫" |
| I | "可以加 1-2 个客户成功故事,有画面感" |
| S | "EBC 节奏控制在他能消化的速度,留足问答时间" |
| C | "确保所有数据可追溯,提供详细的方案文档" |

#### purpose: simulator-roleplay (Phase 1 暂用 pre-visit 兜底)

> Phase 2 用 Hermes Part 5 的 DiSC 中国场景细化内容 + 扮演风格指引完整化。

#### purpose: bttroc-archetype-hint (V2.0 update 2)

> 给 BTTROC 推 5 archetype(Underestimator / Wait-and-see / Risk-Averse / Path-Unclear / Resistant)时的人格倾向 hint。**不下结论**,BTTROC 还要结合 buying behavior + 公开姿态做最终判断。

| 取值 | archetype 倾向 hint |
|---|---|
| D | 倾向 **Underestimator** — 自信、节奏快、不觉得有风险、抗拒被推 |
| I | 倾向 **Path-Unclear** — 看到机会但不清晰路径,愿意被引导 |
| S | 倾向 **Wait-and-see** 或 **Risk-Averse** — 怕变,等市场动 |
| C | 倾向 **Risk-Averse** — 风险敏感、要数据保障 |
| D-I | **Underestimator** 主导 — 自信 + 看到机会想推 |
| D-C | **Resistant** 边缘 — 自信 + 风险敏感容易出现"我自己想清楚就行,不需要你来教" |
| I-S | **Path-Unclear** 偏 **Wait-and-see** — 想动但慢 |
| S-C | **Risk-Averse** 强化 — 慢 + 怕错 |

### 字段:cognitive_function_stack

> **Phase 2 待 V2.0 mbti.md 重写完成后填充完整**(MBTI 重写为功能栈核心)

#### purpose: overview(骨架版)

| 取值 | 大白话(暂版) |
|---|---|
| Ne-Ti | "他对新可能性敏感,但要用内在逻辑过一遍才相信" |
| Te-Ni | "他要可见可执行的成果,会顺手做战略推演" |
| Si-Fe | "他靠经验做判断,关心团队和谐,变化要慢慢推" |
| Ni-Te | "他有自己内在的方向感,执行起来要看效率" |

### 字段:enneagram_motivation

#### purpose: overview(骨架版)

| 取值 | 大白话 |
|---|---|
| 1 | "他追求把事做到完美,看到瑕疵会放大,怕犯错" |
| 3 | "他关心成就和被认可,讲方案讲他能赢什么" |
| 6 | "他重视安全和忠诚,变化让他焦虑,要案例和保障" |
| 8 | "他需要掌控感,被推动会反弹,要让他觉得是他主导" |
| (其他号) | (待 Phase 2 填充) |

#### purpose: bttroc-archetype-hint (V2.0 update 2)

| 取值 | archetype 倾向 hint |
|---|---|
| 1(完美主义) | 倾向 **Wait-and-see** 或 **Risk-Averse** — 怕做错,要"准备好了再动" |
| 2(求被需要) | 倾向 **Path-Unclear** — 看到价值但要被人带 |
| 3(追求成功) | 倾向 **Underestimator** — 自信能搞定,不觉得有风险 |
| 4(求独特) | 倾向 **Path-Unclear** 或 **Resistant** — 不接受标准答案,要走自己的路 |
| 5(求知识) | 倾向 **Risk-Averse** — 想清楚再动,要时间消化 |
| 6(求安全) | 倾向 **Risk-Averse** 经典型 — 怕变化、怕承诺、要案例 |
| 7(求自由) | 倾向 **Underestimator** — 不觉得问题严重,要保留多选项 |
| 8(掌控) | 倾向 **Resistant** 或 **Path-Unclear** — 自己定方向不被推,但若信任来源会接受引导 |
| 9(求和谐) | 倾向 **Wait-and-see** — 不愿冲突,等共识 |

### 字段:fear_pattern

> Phase 2 用 Hermes Part 4 + V2.0 fear-three-rings.md 重构内容填充完整

#### purpose: overview(骨架版)

```
对每个三圈(outer/middle/inner)分别翻译:
- outer (项目层): "他怕这次 [具体描述]"
- middle (声誉层): "他怕在公司里 [具体描述]"
- inner (身份层): "他怕自己变成 [具体描述] 那样的人"
```

#### purpose: bttroc-archetype-hint (V2.0 update 2)

| outer 圈关键词 | archetype 倾向 hint |
|---|---|
| "做错风险" / "投入打水漂" / "影响 KPI" | 倾向 **Risk-Averse** |
| "跟不上" / "被竞品超越" / "落后于行业" | 倾向 **Wait-and-see**(怕做先错) 或 **Path-Unclear**(知道要变但不知道怎么变) |
| "失去权威" / "下属不服" / "出尔反尔" | 倾向 **Resistant** — 强抗拒被推 |
| "看错方向" / "选错路径" | 倾向 **Path-Unclear** — 知道要走但不确定路 |
| outer 全 null(无识别恐惧) | 可能 **Underestimator** — 不觉得有风险所以没识别恐惧 |

> **使用提示**:fear_pattern 三圈完整时(outer + middle + inner 都填),archetype 推断更准。仅 outer 时 hint 仅供参考。

### 字段:trust_stage

#### purpose: overview

| 取值 | 大白话 |
|---|---|
| 陌生供应商 | "你现在对他算什么:陌生供应商。他在评估'你是谁'" |
| 可以合作的一家 | "你现在对他算什么:可以合作的一家。他认可你的能力,但还没把你当首选" |
| 能帮他解决问题的人 | "你现在对他算什么:能帮他解决问题的人。他主动找你帮忙" |
| 他愿意听意见的顾问 | "你现在对他算什么:他愿意听意见的顾问。他征询你的意见,即使不直接相关" |
| 深度绑定的伙伴 | "你现在对他算什么:深度绑定的伙伴。他把你当自己人,内部动态会同步" |

### 字段:china_signals

> Phase 2 用 Hermes Part 4 全部 31 条中国场景虚假信号 + 地域差异填充完整

#### purpose: overview(骨架版)

```
对数组中每条 china_signal:
- "他说了/做了 [signal],在中国商务场景里通常意味着 [interpretation]"
```

### 字段:aspiration_signals + aspiration_status

#### purpose: overview

| 状态 | 大白话呈现 |
|---|---|
| `to_explore` | "他想成为什么样的人:**有几条信号需要继续探索**(下面给你 2-3 个探问句,带去问他自己讲)" |
| `tentatively_understood` | "他想成为什么样的人:**他亲口说过 [客户原话]**,目前理解是 [描述](需要更多场合验证)" |
| `confirmed` | "他想成为什么样的人:[完整描述]" |

#### purpose: pre-visit

`to_explore` 状态时,给 User 探问句模板(从 SKILL.md 取):

```
您在 [X 方向] 上的投入很多,这是这次项目带来的契机,还是您一直在推动的?
听起来您对这个方向有比较深的想法,能聊聊您看到的可能性吗?
如果两年后回头看这一段,您希望那时候的状态是什么样?
```

### 字段:mission_indicators

#### purpose: overview

```
triggered = true:
  "他更大的抱负:[description] — 他不只在做这一单,有更大的事在心里"
triggered = false:
  (不渲染该段,不留空)
```

---

## 自由目的(custom)的处理

如果 User 给的不是预设的 6 种 purpose,而是自由描述(例如"我想了解他对 AI 风险的态度"),Renderer 调用 LLM 解释步骤:

```
LLM Prompt(伪代码):
  以下是 V2.0 翻译模块支持的预设目的:
  [overview, pre-visit, ebc-prep, relationship-review, objection-handling]
  
  以下是 User 描述的本次目的:
  "{custom_purpose_text}"
  
  任务:
  1. 判断 User 的目的最接近哪 1-2 个预设目的
  2. 决定哪些 Record 字段对该目的最相关
  3. 对每个相关字段,基于该目的视角输出一段大白话
     (参考预设目的的措辞风格,确保不出现禁词)
  
  输出 JSON:
  {
    "closest_preset": "...",
    "relevant_fields": ["disc_label", "fear_pattern", ...],
    "translations": {
      "disc_label": "针对 [custom purpose] 视角的大白话",
      ...
    }
  }
```

LLM 解释结果作为本次 View 的临时翻译,**不写回 v2-translator.md**(R13:目的不持久化)。

LLM 解释失败 → 降级到 overview purpose,标注"自由目的解析失败,按总览处理"。

---

## 给其他 skill 维护者:5 步调用指南

如果你是其他 skill 的维护者,想在你的 skill 里使用 Contact Profiling V2.0 的画像数据,按以下 5 步:

### Step 1 · 在你 SKILL.md 的 inputs 里 reference

```yaml
inputs:
  - name: Contact Profile (V2.0 Record)
    repo: GCR-FE/contact-profiling
    schema: CntP_{Customer}_{Name}.md
    required: false / true (你的 skill 决定)
    purpose: 描述你 skill 用 Record 干啥
  - name: Translator Module
    path: contact-profiling/translator/v2-translator.md
    required: false (推荐)
    purpose: 用 purpose=xxx 拿到大白话翻译
```

### Step 2 · 你的 skill 跑的时候,读 2 个文件

- **Record 文件**(已存在 sales 本地路径,例 `~/Documents/AWS-Sales/{Customer}/_account/contacts/CntP_{Customer}_{Name}.md`)
- **Translator markdown**(几 KB 字典文件,本文档)

> ⚠️ **不需要重跑 contact-profiling**。Record 是 user 之前建过的存档,Translator 是字典 — 都是读取,不触发主流程。

### Step 3 · 从 Record 拿你需要的字段

读 Record 顶部的 YAML front-matter,例:

```yaml
disc_label:
  value: "D"
enneagram_motivation:
  value: 8
fear_pattern:
  outer: "团队执行力不够导致战略落地失败"
  middle: "..."
  inner: "..."
```

### Step 4 · 在 Translator 里查表

找 `### 字段:{字段名}` 段 → 找匹配 purpose(你的 skill 场景)→ 取那一格的措辞。

例:你是 BTTROC,要推 archetype:
- 找 `### 字段:disc_label` → `#### purpose: bttroc-archetype-hint` → `D = 倾向 Underestimator`
- 找 `### 字段:enneagram_motivation` → `#### purpose: bttroc-archetype-hint` → `8 = 倾向 Resistant 或 Path-Unclear`
- 综合两条 hint → 推 archetype

### Step 5 · 用翻译措辞作为给 User 的输出

❌ 不要直接写 `DiSC = D`(对 user 不出现理论术语)
✅ 用翻译后的"他做决定时直接,要看结论,不爱铺垫"

---

## Q&A(常见误解)

**Q1:其他 skill 调 Translator,需要先跑一遍 contact-profiling 主流程吗?**

A:**不需要**。
- Record 是 user 之前用 contact-profiling 建过的**存档文件**,已落盘
- Translator 是**字典文件**,纯 markdown 内容
- 下游只读这两份文件,**不触发 contact-profiling 主流程**
- 跟"查英汉词典不需要先学一遍英语"是一回事

**Q2:user 还没建过这个客户的 Record 怎么办?**

A:你的 skill 检查文件存在性,如果 Record 文件不存在:
- 可以 fallback 用 CXO Personas(职位级通用画像)做 placeholder
- 也可以提示 user "还没有这个客户的画像,要不要先建?",由 user 决定是否走 contact-profiling 流程
- **不要被动调用** contact-profiling — 由 user 主动触发(user-in-the-loop)

**Q3:purpose 选哪个?**

A:看你 skill 场景。当前可选(V2.0 update 2):
- `overview` — 完整画像(默认)
- `pre-visit` — 拜访准备(强调如何配合 + 别踩雷)
- `ebc-prep` — EBC 准备(战略对齐)
- `relationship-review` — 关系复盘(推进方向)
- `objection-handling` — 异议应对(回避模式)
- `simulator-roleplay` — Simulator 扮演用
- `bttroc-archetype-hint` — BTTROC 推 archetype 用
- `custom` — 自由场景,LLM 兜底映射

需要新 purpose 时,联系 contact-profiling 维护者(Munkh & Kiro)在 Translator 里加。

**Q4:V2.0 字段名 / 输出语义会改吗?**

A:**V2.0 周期内不改**(R14.3 + R14.4)。可以迭代的只有具体措辞,不动字段名 / 取值范围 / 含义。下游 skill 可以放心 hard-code 字段名。

**Q5:Translator 文档很长,我要全部加进我 skill 上下文吗?**

A:不用。每个 purpose 字段段落用稳定标题格式 `### 字段:{name}` + `#### purpose: {name}`,下游可以**只加载相关字段段**(正则提取),省 token。

**Q6:多个 skill 同时调 Translator 会冲突吗?**

A:不会。Translator 是只读字典文件,无状态、无锁、无并发问题。

---

## 调用方式(机器友好性细节)

**机器友好性**:每个字段段落用稳定的标题格式 `### 字段:{field_name}`,每个 purpose 用 `#### purpose: {purpose_name}`,下游可以正则锚定提取。

**示例 grep**:
```bash
# 提取 disc_label × bttroc-archetype-hint 的翻译规则
sed -n '/### 字段:disc_label/,/### 字段:/p' v2-translator.md | sed -n '/#### purpose: bttroc-archetype-hint/,/#### purpose:/p'
```

---

## 接口稳定承诺 + 演化路径

### V2.0 周期内稳定的(R14.3 / R14.4)

- 所有输入字段名
- 输出语义不变量(每个字段每个取值的"含义")
- 6 个预设 purpose 的覆盖范围

### 可以迭代的

- 每个 purpose 下的具体措辞(可以打磨更精准)
- 翻译规则的具体写法(只要不变 input 字段 + output 含义)
- references 内容演化时同步更新本模块的内部规则

### V2.x / 未来切换为 orchestrator 调度的接口承诺

如果未来切换到 orchestrator 调度模式(OQ-1),下游 Skill 的消费模式不变 — 输入字段、输出语义、purpose 参数全部保持不变,只是"翻译能力放在哪、怎么调用"这个**实现细节**变了。

下游 Skill 的 SKILL.md 不需要改一行(除了 reference 路径可能从文件路径改成调度命名)。

---

## 待 Phase 2 完成的事项

- [ ] DiSC 完整 8 种取值 × 6 种 purpose 的措辞(目前只填了关键 4 种)
- [ ] cognitive_function_stack 完整功能组合 × 6 种 purpose(等 V2.0 mbti.md 重写完成)
- [ ] enneagram_motivation 完整 9 个号 × 6 种 purpose(目前只填 4 个号)
- [ ] fear_pattern 三圈 × 4 个核心职位的常见担心库(用 Hermes Part 4 + 三圈职位库)
- [ ] china_signals 31 条完整翻译(用 Hermes Part 4 全部内容)
- [ ] simulator-roleplay purpose 专属措辞(目前用 pre-visit 兜底)
- [ ] 输出语义稳定承诺表完整化

---

*Munkh & Kiro · 2026-05-17 · Phase 1 骨架版*
