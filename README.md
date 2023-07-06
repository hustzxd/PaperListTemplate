# Paper List Template

This template makes it easy for you to manage papers.

## Table of Contents

- [Paper List Template](#paper-list-template)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
  - [Fast Search](#fast-search)
  - [Paper List](#paper-list)

<details><summary><b>References</b></summary>	
<p>

1. https://github.com/he-y/Awesome-Pruning
2. https://github.com/htqin/awesome-model-quantization
3. https://github.com/csyhhu/Awesome-Deep-Neural-Network-Compression/tree/master
4. https://github.com/AojunZhou/Efficient-Deep-Learning
5. https://github.com/chester256/Model-Compression-Papers

</p>
</details>

## Getting Started
1. Add paper information by `./add_paper_info.sh` or  `./add_paper_info.sh <name>`
2. Run `./refresh_readme.sh`

<details><summary><b>sparsegpt.prototxt</b></summary>	
<p>

```
paper {
  title: "SparseGPT: Massive Language Models Can be Accurately Pruned in one-shot."
  abbr: "SparseGPT"
  url: "https://arxiv.org/pdf/2301.00774.pdf"
  authors: "Elias Frantar"
  authors: "Dan Alistarh"
  institutions: "IST Austria"
  institutions: "Neural Magic"
}
pub {
  where: "arXiv"
  year: 2023
}
code {
  type: "Pytorch"
  url: "https://github.com/IST-DASLab/sparsegpt"
}
note {
  url: "SparseGPT.md"
}
keyword {
  words: "sparsity"
}
```

</p>
</details>




## Fast Search 
<details><summary><b>author</b></summary> 
<p>

1. [Bingzhe-Wu.md](./fast_search/author/Bingzhe-Wu.md) 
1. [Brian-Chmiel.md](./fast_search/author/Brian-Chmiel.md) 
1. [Dan-Alistarh.md](./fast_search/author/Dan-Alistarh.md) 
1. [Daniel-Soudry.md](./fast_search/author/Daniel-Soudry.md) 
1. [Elias-Frantar.md](./fast_search/author/Elias-Frantar.md) 
1. [Ivan-Lazarevich.md](./fast_search/author/Ivan-Lazarevich.md) 
1. [Name1.md](./fast_search/author/Name1.md) 
1. [Name2.md](./fast_search/author/Name2.md) 
1. [Nikita-Malinin.md](./fast_search/author/Nikita-Malinin.md) 
1. [Shiwei-Liu.md](./fast_search/author/Shiwei-Liu.md) 
1. [Zhangyang-Wang.md](./fast_search/author/Zhangyang-Wang.md) 
1. [Zhihang-Yuan.md](./fast_search/author/Zhihang-Yuan.md) 
</p>
</details>
<details><summary><b>year</b></summary> 
<p>

1. [2021.md](./fast_search/year/2021.md) 
1. [2023.md](./fast_search/year/2023.md) 
</p>
</details>
<details><summary><b>pub</b></summary> 
<p>

1. [ICCV-workshop.md](./fast_search/pub/ICCV-workshop.md) 
1. [ICLR.md](./fast_search/pub/ICLR.md) 
1. [arXiv.md](./fast_search/pub/arXiv.md) 
</p>
</details>
<details><summary><b>keyword</b></summary> 
<p>

1. [key1.md](./fast_search/keyword/key1.md) 
1. [key2.md](./fast_search/keyword/key2.md) 
1. [quantization.md](./fast_search/keyword/quantization.md) 
1. [sparse.md](./fast_search/keyword/sparse.md) 
1. [sparsity.md](./fast_search/keyword/sparsity.md) 
</p>
</details>
<details><summary><b>inst</b></summary> 
<p>

1. [Eindhoven-University-of-Technology.md](./fast_search/inst/Eindhoven-University-of-Technology.md) 
1. [Habana-Labs.md](./fast_search/inst/Habana-Labs.md) 
1. [Houmo-AI.md](./fast_search/inst/Houmo-AI.md) 
1. [IST-Austria.md](./fast_search/inst/IST-Austria.md) 
1. [Intel-Corporation.md](./fast_search/inst/Intel-Corporation.md) 
1. [Neural-Magic.md](./fast_search/inst/Neural-Magic.md) 
1. [Tencent-AI-Lab.md](./fast_search/inst/Tencent-AI-Lab.md) 
1. [University-of-Texas-at-Austin.md](./fast_search/inst/University-of-Texas-at-Austin.md) 
1. [inst1.md](./fast_search/inst/inst1.md) 
1. [inst2.md](./fast_search/inst/inst2.md) 
</p>
</details>

## Paper List


### 2023

|    | meta                                   | title                                                                                                                                                                             | publication   |   year | code                                                 | note                         |
|---:|:---------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------|-------:|:-----------------------------------------------------|:-----------------------------|
|  0 | [MVUE](./meta/2U5DXO7C.prototxt)       | [Minimum Variance Unbiased N:M Sparsity for the Neural Gradients](https://openreview.net/pdf?id=vuD2xEtxZcj)                                                                      | ICLR          |   2023 |                                                      |                              |
|  1 | [NTK-SAP](./meta/HYTID4WD.prototxt)    | [NTK-SAP: Improving neural network pruning by aligning training dynamics](https://openreview.net/forum?id=-5EWhW_4qWP)                                                            | ICLR          |   2023 |                                                      |                              |
|  2 | [SMC](./meta/EHWNTP1V.prototxt)        | [Sparsity May Cry: Let Us Fail (Current) Sparse Neural Networks Together!](https://openreview.net/pdf?id=J6F3lLg4Kdp)                                                             | ICLR          |   2023 | [SMC-Bench](https://github.com/VITA-Group/SMC-Bench) |                              |
|  3 | [abbr](./meta/22C0A4RH.prototxt)       | [DFPC: Data flow driven pruning of coupled channels without data](https://openreview.net/forum?id=mhnHqRqcjYU)                                                                    | ICLR          |   2023 |                                                      |                              |
|  4 | [abbr](./meta/JBRI286F.prototxt)       | [CrAM: A Compression-Aware Minimizer](https://openreview.net/forum?id=_eTZBs-yedr)                                                                                                | ICLR          |   2023 |                                                      |                              |
|  5 | [abbr](./meta/MTKTZE3N.prototxt)       | [TVSPrune - Pruning Non-discriminative filters via Total Variation separability of intermediate representations without fine tuning](https://openreview.net/forum?id=sZI1Oj9KBKy) | ICLR          |   2023 |                                                      |                              |
|  6 | [abbr](./meta/Q0PKEEPI.prototxt)       | [HomoDistil: Homotopic Task-Agnostic Distillation of Pre-trained Transformers](https://openreview.net/forum?id=D7srTrGhAs)                                                        | ICLR          |   2023 |                                                      |                              |
|  7 | [abbr](./meta/Q3S45CWC.prototxt)       | [Bit-Pruning: A Sparse Multiplication-Less Dot-Product](https://openreview.net/forum?id=YUDiZcZTI8)                                                                               | ICLR          |   2023 |                                                      |                              |
|  8 | [abbr](./meta/SP5UN1RF.prototxt)       | [A Unified Framework for Soft Threshold Pruning](https://openreview.net/forum?id=cCFqcrq0d8)                                                                                      | ICLR          |   2023 |                                                      |                              |
|  9 | [m](./meta/0I1IQIH6.prototxt)          | [Revisiting Pruning at Initialization Through the Lens of Ramanujan Graph](https://openreview.net/forum?id=uVcDssQff)                                                             | ICLR          |   2023 |                                                      |                              |
| 10 | [m](./meta/R4X91L5N.prototxt)          | [Unmasking the Lottery Ticket Hypothesis: What's Encoded in a Winning Ticket's Mask?](https://openreview.net/forum?id=xSsW2Am-ukZ)                                                | ICLR          |   2023 |                                                      |                              |
| 11 | [RPTQ](./meta/RPTQ.prototxt)           | [RPTQ: Reorder-based Post-training Quantization for Large Language Models](https://arxiv.org/pdf/2304.01089.pdf)                                                                  | arXiv         |   2023 | [PyTorch](https://github.com/hahnyuan/RPTQ4LLM)      |                              |
| 12 | [SparseGPT](./meta/sparsegpt.prototxt) | [SparseGPT: Massive Language Models Can be Accurately Pruned in one-shot.](https://arxiv.org/pdf/2301.00774.pdf)                                                                  | arXiv         |   2023 | [Pytorch](https://github.com/IST-DASLab/sparsegpt)   | [note](./notes/SparseGPT.md) |
### 2021

|    | meta                                 | title                                                                                                                                                                                                                                    | publication   |   year | code   | note   |
|---:|:-------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------|-------:|:-------|:-------|
|  0 | [OpenVINO](./meta/OpenVINO.prototxt) | [Post-training deep neural network pruning via layer-wise calibration](https://openaccess.thecvf.com/content/ICCV2021W/LPCV/papers/Lazarevich_Post-Training_Deep_Neural_Network_Pruning_via_Layer-Wise_Calibration_ICCVW_2021_paper.pdf) | ICCV workshop |   2021 |        |        |