# Paper List Template

This template makes it easy for you to manage papers.

## Table of Contents

- [Paper List Template](#paper-list-template)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)


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



## Paper List

<details open><summary>

### keyword
</summary>
<p>

<details open><summary><b>Quantization</b></summary>
<p>

|    | meta                         | title                                                                                                            | publication   |   year | code                                            | note   | cover   |
|---:|:-----------------------------|:-----------------------------------------------------------------------------------------------------------------|:--------------|-------:|:------------------------------------------------|:-------|:--------|
|  0 | [RPTQ](./meta/RPTQ.prototxt) | [RPTQ: Reorder-based Post-training Quantization for Large Language Models](https://arxiv.org/pdf/2304.01089.pdf) | arXiv         |   2023 | [PyTorch](https://github.com/hahnyuan/RPTQ4LLM) |        |         |</p>
</details>
<details open><summary><b>Sparse/Pruning</b></summary>
<p>

|    | meta                                   | title                                                                                                                                                                                                                                    | publication   |   year | code                                                 | note                                   | cover                                                            |
|---:|:---------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------|-------:|:-----------------------------------------------------|:---------------------------------------|:-----------------------------------------------------------------|
|  0 | [OpenVINO](./meta/OpenVINO.prototxt)   | [Post-training deep neural network pruning via layer-wise calibration](https://openaccess.thecvf.com/content/ICCV2021W/LPCV/papers/Lazarevich_Post-Training_Deep_Neural_Network_Pruning_via_Layer-Wise_Calibration_ICCVW_2021_paper.pdf) | ICCV workshop |   2021 |                                                      |                                        |                                                                  |
|  1 | [MVUE](./meta/2U5DXO7C.prototxt)       | [Minimum Variance Unbiased N:M Sparsity for the Neural Gradients](https://openreview.net/pdf?id=vuD2xEtxZcj)                                                                                                                             | ICLR          |   2023 |                                                      |                                        |                                                                  |
|  2 | [SMC](./meta/EHWNTP1V.prototxt)        | [Sparsity May Cry: Let Us Fail (Current) Sparse Neural Networks Together!](https://openreview.net/pdf?id=J6F3lLg4Kdp)                                                                                                                    | ICLR          |   2023 | [SMC-Bench](https://github.com/VITA-Group/SMC-Bench) |                                        |                                                                  |
|  3 | [SparseGPT](./meta/sparsegpt.prototxt) | [SparseGPT: Massive Language Models Can be Accurately Pruned in one-shot.](https://arxiv.org/pdf/2301.00774.pdf)                                                                                                                         | arXiv         |   2023 | [Pytorch](https://github.com/IST-DASLab/sparsegpt)   | [note](./notes/sparsegpt/SparseGPT.md) | <img width='1000' alt='image' src='./notes/sparsegpt/cover.jpg'> |</p>
</details>
</p>
</details>

<details><summary>

### year
</summary>
<p>

<details><summary><b>2021</b></summary>
<p>

|    | meta                                 | title                                                                                                                                                                                                                                    | publication   |   year | code   | note   | cover   |
|---:|:-------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------|-------:|:-------|:-------|:--------|
|  0 | [OpenVINO](./meta/OpenVINO.prototxt) | [Post-training deep neural network pruning via layer-wise calibration](https://openaccess.thecvf.com/content/ICCV2021W/LPCV/papers/Lazarevich_Post-Training_Deep_Neural_Network_Pruning_via_Layer-Wise_Calibration_ICCVW_2021_paper.pdf) | ICCV workshop |   2021 |        |        |         |</p>
</details>
<details><summary><b>2023</b></summary>
<p>

|    | meta                                   | title                                                                                                                 | publication   |   year | code                                                 | note                                   | cover                                                            |
|---:|:---------------------------------------|:----------------------------------------------------------------------------------------------------------------------|:--------------|-------:|:-----------------------------------------------------|:---------------------------------------|:-----------------------------------------------------------------|
|  0 | [MVUE](./meta/2U5DXO7C.prototxt)       | [Minimum Variance Unbiased N:M Sparsity for the Neural Gradients](https://openreview.net/pdf?id=vuD2xEtxZcj)          | ICLR          |   2023 |                                                      |                                        |                                                                  |
|  1 | [SMC](./meta/EHWNTP1V.prototxt)        | [Sparsity May Cry: Let Us Fail (Current) Sparse Neural Networks Together!](https://openreview.net/pdf?id=J6F3lLg4Kdp) | ICLR          |   2023 | [SMC-Bench](https://github.com/VITA-Group/SMC-Bench) |                                        |                                                                  |
|  2 | [RPTQ](./meta/RPTQ.prototxt)           | [RPTQ: Reorder-based Post-training Quantization for Large Language Models](https://arxiv.org/pdf/2304.01089.pdf)      | arXiv         |   2023 | [PyTorch](https://github.com/hahnyuan/RPTQ4LLM)      |                                        |                                                                  |
|  3 | [SparseGPT](./meta/sparsegpt.prototxt) | [SparseGPT: Massive Language Models Can be Accurately Pruned in one-shot.](https://arxiv.org/pdf/2301.00774.pdf)      | arXiv         |   2023 | [Pytorch](https://github.com/IST-DASLab/sparsegpt)   | [note](./notes/sparsegpt/SparseGPT.md) | <img width='1000' alt='image' src='./notes/sparsegpt/cover.jpg'> |</p>
</details>
</p>
</details>

<details><summary>

### publication
</summary>
<p>

<details><summary><b>ICCV workshop</b></summary>
<p>

|    | meta                                 | title                                                                                                                                                                                                                                    | publication   |   year | code   | note   | cover   |
|---:|:-------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------|-------:|:-------|:-------|:--------|
|  0 | [OpenVINO](./meta/OpenVINO.prototxt) | [Post-training deep neural network pruning via layer-wise calibration](https://openaccess.thecvf.com/content/ICCV2021W/LPCV/papers/Lazarevich_Post-Training_Deep_Neural_Network_Pruning_via_Layer-Wise_Calibration_ICCVW_2021_paper.pdf) | ICCV workshop |   2021 |        |        |         |</p>
</details>
<details><summary><b>ICLR</b></summary>
<p>

|    | meta                             | title                                                                                                                 | publication   |   year | code                                                 | note   | cover   |
|---:|:---------------------------------|:----------------------------------------------------------------------------------------------------------------------|:--------------|-------:|:-----------------------------------------------------|:-------|:--------|
|  0 | [MVUE](./meta/2U5DXO7C.prototxt) | [Minimum Variance Unbiased N:M Sparsity for the Neural Gradients](https://openreview.net/pdf?id=vuD2xEtxZcj)          | ICLR          |   2023 |                                                      |        |         |
|  1 | [SMC](./meta/EHWNTP1V.prototxt)  | [Sparsity May Cry: Let Us Fail (Current) Sparse Neural Networks Together!](https://openreview.net/pdf?id=J6F3lLg4Kdp) | ICLR          |   2023 | [SMC-Bench](https://github.com/VITA-Group/SMC-Bench) |        |         |</p>
</details>
<details><summary><b>arXiv</b></summary>
<p>

|    | meta                                   | title                                                                                                            | publication   |   year | code                                               | note                                   | cover                                                            |
|---:|:---------------------------------------|:-----------------------------------------------------------------------------------------------------------------|:--------------|-------:|:---------------------------------------------------|:---------------------------------------|:-----------------------------------------------------------------|
|  0 | [RPTQ](./meta/RPTQ.prototxt)           | [RPTQ: Reorder-based Post-training Quantization for Large Language Models](https://arxiv.org/pdf/2304.01089.pdf) | arXiv         |   2023 | [PyTorch](https://github.com/hahnyuan/RPTQ4LLM)    |                                        |                                                                  |
|  1 | [SparseGPT](./meta/sparsegpt.prototxt) | [SparseGPT: Massive Language Models Can be Accurately Pruned in one-shot.](https://arxiv.org/pdf/2301.00774.pdf) | arXiv         |   2023 | [Pytorch](https://github.com/IST-DASLab/sparsegpt) | [note](./notes/sparsegpt/SparseGPT.md) | <img width='1000' alt='image' src='./notes/sparsegpt/cover.jpg'> |</p>
</details>
</p>
</details>

<details><summary>

### instution
</summary>
<p>

<details><summary><b>Eindhoven University of Technology</b></summary>
<p>

|    | meta                            | title                                                                                                                 | publication   |   year | code                                                 | note   | cover   |
|---:|:--------------------------------|:----------------------------------------------------------------------------------------------------------------------|:--------------|-------:|:-----------------------------------------------------|:-------|:--------|
|  0 | [SMC](./meta/EHWNTP1V.prototxt) | [Sparsity May Cry: Let Us Fail (Current) Sparse Neural Networks Together!](https://openreview.net/pdf?id=J6F3lLg4Kdp) | ICLR          |   2023 | [SMC-Bench](https://github.com/VITA-Group/SMC-Bench) |        |         |</p>
</details>
<details><summary><b>Habana Labs</b></summary>
<p>

|    | meta                             | title                                                                                                        | publication   |   year | code   | note   | cover   |
|---:|:---------------------------------|:-------------------------------------------------------------------------------------------------------------|:--------------|-------:|:-------|:-------|:--------|
|  0 | [MVUE](./meta/2U5DXO7C.prototxt) | [Minimum Variance Unbiased N:M Sparsity for the Neural Gradients](https://openreview.net/pdf?id=vuD2xEtxZcj) | ICLR          |   2023 |        |        |         |</p>
</details>
<details><summary><b>Houmo AI</b></summary>
<p>

|    | meta                         | title                                                                                                            | publication   |   year | code                                            | note   | cover   |
|---:|:-----------------------------|:-----------------------------------------------------------------------------------------------------------------|:--------------|-------:|:------------------------------------------------|:-------|:--------|
|  0 | [RPTQ](./meta/RPTQ.prototxt) | [RPTQ: Reorder-based Post-training Quantization for Large Language Models](https://arxiv.org/pdf/2304.01089.pdf) | arXiv         |   2023 | [PyTorch](https://github.com/hahnyuan/RPTQ4LLM) |        |         |</p>
</details>
<details><summary><b>IST Austria</b></summary>
<p>

|    | meta                                   | title                                                                                                            | publication   |   year | code                                               | note                                   | cover                                                            |
|---:|:---------------------------------------|:-----------------------------------------------------------------------------------------------------------------|:--------------|-------:|:---------------------------------------------------|:---------------------------------------|:-----------------------------------------------------------------|
|  0 | [SparseGPT](./meta/sparsegpt.prototxt) | [SparseGPT: Massive Language Models Can be Accurately Pruned in one-shot.](https://arxiv.org/pdf/2301.00774.pdf) | arXiv         |   2023 | [Pytorch](https://github.com/IST-DASLab/sparsegpt) | [note](./notes/sparsegpt/SparseGPT.md) | <img width='1000' alt='image' src='./notes/sparsegpt/cover.jpg'> |</p>
</details>
<details><summary><b>Intel Corporation</b></summary>
<p>

|    | meta                                 | title                                                                                                                                                                                                                                    | publication   |   year | code   | note   | cover   |
|---:|:-------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------|-------:|:-------|:-------|:--------|
|  0 | [OpenVINO](./meta/OpenVINO.prototxt) | [Post-training deep neural network pruning via layer-wise calibration](https://openaccess.thecvf.com/content/ICCV2021W/LPCV/papers/Lazarevich_Post-Training_Deep_Neural_Network_Pruning_via_Layer-Wise_Calibration_ICCVW_2021_paper.pdf) | ICCV workshop |   2021 |        |        |         |</p>
</details>
<details><summary><b>Neural Magic</b></summary>
<p>

|    | meta                                   | title                                                                                                            | publication   |   year | code                                               | note                                   | cover                                                            |
|---:|:---------------------------------------|:-----------------------------------------------------------------------------------------------------------------|:--------------|-------:|:---------------------------------------------------|:---------------------------------------|:-----------------------------------------------------------------|
|  0 | [SparseGPT](./meta/sparsegpt.prototxt) | [SparseGPT: Massive Language Models Can be Accurately Pruned in one-shot.](https://arxiv.org/pdf/2301.00774.pdf) | arXiv         |   2023 | [Pytorch](https://github.com/IST-DASLab/sparsegpt) | [note](./notes/sparsegpt/SparseGPT.md) | <img width='1000' alt='image' src='./notes/sparsegpt/cover.jpg'> |</p>
</details>
<details><summary><b>Tencent AI Lab</b></summary>
<p>

|    | meta                         | title                                                                                                            | publication   |   year | code                                            | note   | cover   |
|---:|:-----------------------------|:-----------------------------------------------------------------------------------------------------------------|:--------------|-------:|:------------------------------------------------|:-------|:--------|
|  0 | [RPTQ](./meta/RPTQ.prototxt) | [RPTQ: Reorder-based Post-training Quantization for Large Language Models](https://arxiv.org/pdf/2304.01089.pdf) | arXiv         |   2023 | [PyTorch](https://github.com/hahnyuan/RPTQ4LLM) |        |         |</p>
</details>
<details><summary><b>University of Texas at Austin</b></summary>
<p>

|    | meta                            | title                                                                                                                 | publication   |   year | code                                                 | note   | cover   |
|---:|:--------------------------------|:----------------------------------------------------------------------------------------------------------------------|:--------------|-------:|:-----------------------------------------------------|:-------|:--------|
|  0 | [SMC](./meta/EHWNTP1V.prototxt) | [Sparsity May Cry: Let Us Fail (Current) Sparse Neural Networks Together!](https://openreview.net/pdf?id=J6F3lLg4Kdp) | ICLR          |   2023 | [SMC-Bench](https://github.com/VITA-Group/SMC-Bench) |        |         |</p>
</details>
</p>
</details>

<details><summary>

### author
</summary>
<p>

<details><summary><b>Bingzhe Wu</b></summary>
<p>

|    | meta                         | title                                                                                                            | publication   |   year | code                                            | note   | cover   |
|---:|:-----------------------------|:-----------------------------------------------------------------------------------------------------------------|:--------------|-------:|:------------------------------------------------|:-------|:--------|
|  0 | [RPTQ](./meta/RPTQ.prototxt) | [RPTQ: Reorder-based Post-training Quantization for Large Language Models](https://arxiv.org/pdf/2304.01089.pdf) | arXiv         |   2023 | [PyTorch](https://github.com/hahnyuan/RPTQ4LLM) |        |         |</p>
</details>
<details><summary><b>Brian Chmiel</b></summary>
<p>

|    | meta                             | title                                                                                                        | publication   |   year | code   | note   | cover   |
|---:|:---------------------------------|:-------------------------------------------------------------------------------------------------------------|:--------------|-------:|:-------|:-------|:--------|
|  0 | [MVUE](./meta/2U5DXO7C.prototxt) | [Minimum Variance Unbiased N:M Sparsity for the Neural Gradients](https://openreview.net/pdf?id=vuD2xEtxZcj) | ICLR          |   2023 |        |        |         |</p>
</details>
<details><summary><b>Dan Alistarh</b></summary>
<p>

|    | meta                                   | title                                                                                                            | publication   |   year | code                                               | note                                   | cover                                                            |
|---:|:---------------------------------------|:-----------------------------------------------------------------------------------------------------------------|:--------------|-------:|:---------------------------------------------------|:---------------------------------------|:-----------------------------------------------------------------|
|  0 | [SparseGPT](./meta/sparsegpt.prototxt) | [SparseGPT: Massive Language Models Can be Accurately Pruned in one-shot.](https://arxiv.org/pdf/2301.00774.pdf) | arXiv         |   2023 | [Pytorch](https://github.com/IST-DASLab/sparsegpt) | [note](./notes/sparsegpt/SparseGPT.md) | <img width='1000' alt='image' src='./notes/sparsegpt/cover.jpg'> |</p>
</details>
<details><summary><b>Daniel Soudry</b></summary>
<p>

|    | meta                             | title                                                                                                        | publication   |   year | code   | note   | cover   |
|---:|:---------------------------------|:-------------------------------------------------------------------------------------------------------------|:--------------|-------:|:-------|:-------|:--------|
|  0 | [MVUE](./meta/2U5DXO7C.prototxt) | [Minimum Variance Unbiased N:M Sparsity for the Neural Gradients](https://openreview.net/pdf?id=vuD2xEtxZcj) | ICLR          |   2023 |        |        |         |</p>
</details>
<details><summary><b>Elias Frantar</b></summary>
<p>

|    | meta                                   | title                                                                                                            | publication   |   year | code                                               | note                                   | cover                                                            |
|---:|:---------------------------------------|:-----------------------------------------------------------------------------------------------------------------|:--------------|-------:|:---------------------------------------------------|:---------------------------------------|:-----------------------------------------------------------------|
|  0 | [SparseGPT](./meta/sparsegpt.prototxt) | [SparseGPT: Massive Language Models Can be Accurately Pruned in one-shot.](https://arxiv.org/pdf/2301.00774.pdf) | arXiv         |   2023 | [Pytorch](https://github.com/IST-DASLab/sparsegpt) | [note](./notes/sparsegpt/SparseGPT.md) | <img width='1000' alt='image' src='./notes/sparsegpt/cover.jpg'> |</p>
</details>
<details><summary><b>Ivan Lazarevich</b></summary>
<p>

|    | meta                                 | title                                                                                                                                                                                                                                    | publication   |   year | code   | note   | cover   |
|---:|:-------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------|-------:|:-------|:-------|:--------|
|  0 | [OpenVINO](./meta/OpenVINO.prototxt) | [Post-training deep neural network pruning via layer-wise calibration](https://openaccess.thecvf.com/content/ICCV2021W/LPCV/papers/Lazarevich_Post-Training_Deep_Neural_Network_Pruning_via_Layer-Wise_Calibration_ICCVW_2021_paper.pdf) | ICCV workshop |   2021 |        |        |         |</p>
</details>
<details><summary><b>Nikita Malinin</b></summary>
<p>

|    | meta                                 | title                                                                                                                                                                                                                                    | publication   |   year | code   | note   | cover   |
|---:|:-------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------|-------:|:-------|:-------|:--------|
|  0 | [OpenVINO](./meta/OpenVINO.prototxt) | [Post-training deep neural network pruning via layer-wise calibration](https://openaccess.thecvf.com/content/ICCV2021W/LPCV/papers/Lazarevich_Post-Training_Deep_Neural_Network_Pruning_via_Layer-Wise_Calibration_ICCVW_2021_paper.pdf) | ICCV workshop |   2021 |        |        |         |</p>
</details>
<details><summary><b>Shiwei Liu</b></summary>
<p>

|    | meta                            | title                                                                                                                 | publication   |   year | code                                                 | note   | cover   |
|---:|:--------------------------------|:----------------------------------------------------------------------------------------------------------------------|:--------------|-------:|:-----------------------------------------------------|:-------|:--------|
|  0 | [SMC](./meta/EHWNTP1V.prototxt) | [Sparsity May Cry: Let Us Fail (Current) Sparse Neural Networks Together!](https://openreview.net/pdf?id=J6F3lLg4Kdp) | ICLR          |   2023 | [SMC-Bench](https://github.com/VITA-Group/SMC-Bench) |        |         |</p>
</details>
<details><summary><b>Zhangyang Wang</b></summary>
<p>

|    | meta                            | title                                                                                                                 | publication   |   year | code                                                 | note   | cover   |
|---:|:--------------------------------|:----------------------------------------------------------------------------------------------------------------------|:--------------|-------:|:-----------------------------------------------------|:-------|:--------|
|  0 | [SMC](./meta/EHWNTP1V.prototxt) | [Sparsity May Cry: Let Us Fail (Current) Sparse Neural Networks Together!](https://openreview.net/pdf?id=J6F3lLg4Kdp) | ICLR          |   2023 | [SMC-Bench](https://github.com/VITA-Group/SMC-Bench) |        |         |</p>
</details>
<details><summary><b>Zhihang Yuan</b></summary>
<p>

|    | meta                         | title                                                                                                            | publication   |   year | code                                            | note   | cover   |
|---:|:-----------------------------|:-----------------------------------------------------------------------------------------------------------------|:--------------|-------:|:------------------------------------------------|:-------|:--------|
|  0 | [RPTQ](./meta/RPTQ.prototxt) | [RPTQ: Reorder-based Post-training Quantization for Large Language Models](https://arxiv.org/pdf/2304.01089.pdf) | arXiv         |   2023 | [PyTorch](https://github.com/hahnyuan/RPTQ4LLM) |        |         |</p>
</details>
</p>
</details>


## References

1. https://github.com/he-y/Awesome-Pruning
2. https://github.com/htqin/awesome-model-quantization
3. https://github.com/csyhhu/Awesome-Deep-Neural-Network-Compression/tree/master
4. https://github.com/AojunZhou/Efficient-Deep-Learning
5. https://github.com/chester256/Model-Compression-Papers
