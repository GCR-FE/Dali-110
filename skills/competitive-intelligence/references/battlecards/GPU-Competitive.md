---
title: GPU 竞争分析 — AWS vs Azure / GCP / 阿里云 / OCI / CoreWeave
type: battlecard
scope: gpu-genai
sources:
  - raw/CI Database/GPU Competitive Analysis.pdf
last_updated: 2026-05-13
status: stable
tags: [battlecard, gpu, genai, h100, h200, b200, gb200, trainium, ultracluster, efa]
internal_only: true
---

# GPU / 生成式 AI 竞争分析 Battlecard

> ⚠️ CI 内部使用。源文档 28 页，本页提炼核心打法、对比表、定价。

## TL;DR — AWS GPU 4 大优势

| 维度 | AWS 关键能力 | 量化指标 |
|---|---|---|
| **1. 超强可扩展性** | UltraCluster + EFA | 单集群 **20K H200/H100** 或 **100K Trainium**；3.2 Tbps 带宽；4th Gen EFA 比传统 fabric **16× scale + 更低延迟** |
| **2. 存储优势** | FSx for Lustre + S3 + EFS | S3 Express One Zone：**2M 读 / 200K 写/秒**（100x boost）；FSx Lustre：**1TB/s+ 吞吐** |
| **3. 可靠性 + 安全** | Nitro System | 硬件级加密（NCCL/EFA 透明加解密）+ 物理基础设施验证 |
| **4. 服务灵活性** | EC2 自建 / EKS-ECS 容器 / SageMaker 全托管 | HyperPod 自动恢复**减少停机 40%**；Endpoints 多模型部署**降本 50%**；Spot **降本 90%** |

---

## 1. 核心 Sales Plays（讲给客户）

### 1.1 Project Ceiba — NVIDIA 自己也用 AWS

NVIDIA 内部 R&D AI 超算 Project Ceiba 部署在 AWS：
- **414 EXAFLOPS 算力**
- **20,736 GB200 superchip**
- Gen 4 EFA + UltraClusters + Nitro
- > 世界最快 AI 超算，由 AWS 提供
- > NVIDIA 选择 AWS 是因为 EFA 让他们能在自家芯片设计上快速创新

### 1.2 关键说服点
1. **客户工作负载映射 AWS GPU 服务** — 也考虑 Trainium/Inferentia
2. **性能/成本权衡** — 与 AWS 专家共同评估
3. **从 PoC 开始** — 体验 AWS 差异

---

## 2. 对象存储对比表（GenAI 训练数据基础）

| 维度 | **AWS S3** | Azure Blob | GCP Cloud Storage | 阿里 OSS | 腾讯 COS | OCI |
|---|---|---|---|---|---|---|
| **容量上限** | **无限** ✓ | 500TB/账户（可申请扩） | 无限+配额 | 无限/单实例 48.8TB | 无限/单实例 48.8TB | 10PB/namespace |
| **延迟** | Standard 10-100ms / **Express One Zone 个位数 ms** ✓**（10x faster）** | 10-100ms / Premium 5-20ms | 10-50ms / Premium 5-15ms | 5-20ms / Premium 2-10ms | 10-30ms / Premium 5-15ms | 10-50ms / Premium 5-15ms |
| **请求速率** | Standard **3.5K PUT/5.5K GET 每分区**；**Express One Zone：2M 读 / 200K 写**✓**（100× boost）** | 20K req/s | 1K req/s | 10K req/s | 30K req/s | 1K req/s |
| **并发连接** | 无限 / Express One Zone：**协同高位优化** | 500/blob | 无明确限制 | 无明确限制 | 无明确限制 | 无明确限制 |
| **成本优化** | 3 层 + Intelligent Tiering + Glacier；**请求成本降 50%** | 3-4 层 Hot/Cool/Archive | 4 层自动分层 | 4 层智能分层 | 4 层智能分层 | 3 层 + 分层 |
| **ML 集成** | **SageMaker/Bedrock 原生 + Express One Zone 推理优化** ✓ | Azure ML | Vertex AI | PAI | TI-ONE | OCI Data Science |

---

## 3. 文件系统对比（H100/B200 训练高吞吐场景）

| 维度 | AWS | Azure | GCP | 阿里云 | 腾讯云 | OCI |
|---|---|---|---|---|---|---|
| **服务** | **FSx Lustre + EFS** ✓ | HPC Cache, NetApp | Filestore | CPFS | CFS | FSS |
| **最大吞吐** | **Lustre 1TB/s+；FSx SSD 4TB/s；EFS 60 GiB/s** | 75 GB/s | 16 GB/s | 150 GB/s | 40 GB/s | 27 GB/s |
| **最大 IOPS** | **EFS 2.5M / FSx 几十万** | 460K | 100K | 1.5M | 1M | 500K |
| **延迟** | **EFS 250μs / FSx sub-ms** ✓ | 1-2ms | 1-2ms | sub-ms | 1-3ms | 1-2ms |
| **存储介质** | **SSD/HDD/智能分层** ✓ | SSD/HDD 分层无智能 | SSD/HDD 无智能 | SSD/HDD 有智能 | SSD/HDD 有智能 | SSD/HDD 无智能 |
| **弹性** | **完全弹性扩展** ✓ | 需容量规划 | 需容量规划 | 需容量规划 | 需容量规划 | 需容量规划 |

> 阿里云 CPFS 在 IOPS 数据上看起来高，但缺**统一智能分层**和**ML 服务原生集成**。

---

## 4. H100 / H200 / B200 关键对比

### 4.1 H100 8GPU 实例（单机配置）

| | **AWS P5.48xlarge** | Azure ND96isr H100 v5 | Azure NCads_H100_v5 (PCIe) | GCP a3-megagpu-8g | OCI BM.GPU.H100 | CoreWeave HGX H100 |
|---|---|---|---|---|---|---|
| GPU 数 | 8 | 8 | 1/2 | 1/2/4/8 | 8 | 8 |
| RDMA | **32×100Gbps EFAv2** | 8×400Gbps **IB** | **无 RDMA**（仅 80Gbps 普通带宽） | (8+1)×200 GPUDirect-TCPXO | 8×2×200 RDMA | 3200 Gbps |
| GPU P2P | **NVSwitch 900 GB/s** | NVLink 900 | / | NVLink 900 | NVSwitch+NVLink 4.0 | NVLink 900 |
| 存储 SSD | 8×3.84 TiB NVMe | 28000 GiB | 7152 | 6000 | 16×3.84TB | 61.44 TB |
| 实例内存 | 2 TiB | 1900 GiB | 640 | 1872 | 2048 | 2048 |

> **AliCloud / 腾讯云 / 华为云不提供 H100/H200/B200**——美国 2024 芯片管制；H20 通过白名单仅在阿里云法兰克福/中国大陆可用，**H20 是 H100 的低端版本**。

### 4.2 RDMA 实现对比

| 厂商 | RDMA 实现 | 多 GPU 集群网络性能 |
|---|---|---|
| **AWS** | **EFA + Nitro/EC2 优化栈** | **业内领先低延迟 + scale** ✓ |
| GCP | 自研 RDMA NIC（H100）/ Nvidia RoCE（H200/B200/GB200） | RDMA 平均，RoCE 可能最佳 |
| Azure | IB | 可能最佳（有 IB） |
| 阿里云 | eRDMA 自研 / Stella 定制 RoCE | N/A（仅 H20） |
| OCI | RoCEv2 + IB（GB200） | 可能最佳；可 scale 131K GPU（数据中心是否同一存疑） |
| CoreWeave | IB | 可能最佳（IB） |

---

## 5. UltraCluster 独家优势

支持实例：**P6, P5en, P5e, P5, P4d, TRN2, TRN1**

- **Petabit-scale 无阻塞 fabric**
- **20,000 H200/H100 GPU** 或 **100,000 Trainium**
- **4th-Gen EFA**：16× scale + 更低延迟，3.2 Tbps（P6-B200）
- 集成 **GPUDirect RDMA** 加速器到加速器超低延迟
- **FSx Lustre sub-ms** + S3 无限分层

---

## 6. H200 定价对比（弗吉尼亚）— **AWS 全面胜出**

| 模型 | **AWS P5en.48xlarge** | GCP a3-ultragpu-8g | Azure ND96isr H200 v5 | 阿里云 gn8v-8x.48xlarge (H20) |
|---|---|---|---|---|
| **OD** | $63.30 | $84.94（实际不支持OD） | $84.80 | $55.08 |
| **1Y RI/SP** | **CSP $49.85（21% off）/ ISP $34.68（37% off）** | $58.55（31% off） | $45.22（47% off） | $36.22（34% off） |
| **3Y RI/SP** | **CSP $46.52 / ISP $27.34（57% off）** ✓**最低价** | $37.27（56% off） | $37.31（56% off） | $36.22（34% off） |
| **Spot** | **$18.31（71% off）** ✓**Spot 最低** | $33.96（60% off） | $84.80（**0% off**） | N/A |
| **Capacity Blocks** | **$36.18（43% off）** | Calendar $59.36（30% off） | N/A | N/A |
| **其他** | — | Flex-start $42.4（50% off） | — | Monthly RI $36.22 |

> **客户最常用**：3Y ISP 或 Spot — AWS **3Y ISP $27.34** 是市场最低；Spot $18.31 比 GCP 便宜 46%。

---

## 7. Capacity Block (AWS) vs DWS (GCP) 关键对比

| 维度 | AWS Capacity Blocks | GCP DWS |
|---|---|---|
| 实例 | GB200/B200/H200/H100/A100/Trainium 全覆盖 | B200, H200 |
| 单次预订上限 | **64 实例/请求，256 总量** | 1-80 实例/请求 |
| 时长 | **短：1-14 天；长：7-128 天** | 1-90 天 |
| 提前预订上限 | **8 周（56 天）** | GPU 60 天 / TPU 120 天 |
| 提前预订下限 | **30 分钟** ✓ | GPU 87h / TPU 24h |
| 跨账户共享 | 否 | 是（最多 100 项目，需创建前指定） |
| **最大折扣** | **60% off OD** | H200 30% off OD |
| 可用区域 | **15 个** | 9 个 |

---

## 8. SageMaker 服务灵活性（仅 AWS 提供完整三档）

| 选项 | 适用 | 关键能力 |
|---|---|---|
| **SageMaker HyperPod** | 半托管分布式 GPU 集群 | **训练任务自动恢复，停机减 40%** |
| **SageMaker Endpoints** | 弹性可扩展推理 GPU 节点 | 多容器/多模型部署，**降本 50%**；一键大模型部署 |
| **SageMaker Training Jobs** | 全托管训练 GPU 资源池 | 按任务付费无长期承诺；**Spot 降本 90%** |

---

## 9. 关键 FAQ（销售常被问）

| Q | A |
|---|---|
| **GCP 文档说 3.6 Tbps，AWS 3.2 Tbps？** | GCP 3.6 = 3.2 RDMA + 0.4 通用网络。**真正高性能 GPU 工作负载用 RDMA = 3.2 Tbps（与 AWS 相同）** |
| **GCP GPU 支持 InfiniBand 吗？** | **不支持 IB**。用 CX-7 + RoCE v2；H200/B200/GB200 用 Nvidia RoCE NIC |
| **A100 80GB vs 40GB 性能差距？** | 算力相同；80GB 内存大、带宽高。**小 batch/小模型差不多；大 batch/大模型 80GB 优势明显** |
| **阿里云能合规提供 RTX 4090 / H100？** | **不能**。RTX 4090 违反 NVIDIA 商用条款（消费卡禁数据中心）；H100 NVIDIA 已暂停对阿里销售，未来合规风险 |
| **影响训练/推理性能的 GPU 指标？** | 7 项：算力（Tensor/CUDA）、HBM 带宽、节点内 GPU 互联（NVLink/NVSwitch/PCIe）、P2P 启用、H2D/D2H 带宽、PCIe 拓扑、网络带宽（RDMA 是否独占） |

---

## 10. Field Guidance — 销售战术

1. **打加速计算独特优势**——区分其他厂商
2. **看全景，熟悉各厂商优劣**
3. **深入每家定价策略**——客户最常用 3Y ISP 和 Spot，AWS 最便宜
4. **engage CI 团队**——开 SpecReq 1:1 deal support

---

## 关联页面
- [[Compete/AliCloud]] — 阿里云全面竞争
- [[Compete/Azure]] — Azure 中国出海
- [[Battlecards/FSI-Fraud-AI]] — FSI GPU 用例
- [[Methodology/MEDDPICC-2026]]
