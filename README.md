# EfficientPaper
Pruning, Quantization and efficient-inference/training paper list.

https://github.com/he-y/Awesome-Pruning

https://github.com/htqin/awesome-model-quantization

https://github.com/csyhhu/Awesome-Deep-Neural-Network-Compression/tree/master

https://github.com/AojunZhou/Efficient-Deep-Learning

https://github.com/chester256/Model-Compression-Papers

1. Add meta information in ./meta
2. Run `python scripts/generate_paper_list.py`


|    | meta                           | title                                                                                                                                                                                                                                                | publication        | code                                                 | note                         |
|---:|:-------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|:-----------------------------------------------------|:-----------------------------|
|  0 | [m](./meta/EHWNTP1V.prototxt)  | [ (SMC) Sparsity May Cry: Let Us Fail (Current) Sparse Neural Networks Together!](https://openreview.net/pdf?id=J6F3lLg4Kdp)                                                                                                                         | ICLR-2023          | [SMC-Bench](https://github.com/VITA-Group/SMC-Bench) |                              |
|  1 | [m](./meta/RPTQ.prototxt)      | [ (RPTQ) RPTQ: Reorder-based Post-training Quantization for Large Language Models](https://arxiv.org/pdf/2304.01089.pdf)                                                                                                                             | arXiv-2023         | [PyTorch](https://github.com/hahnyuan/RPTQ4LLM)      |                              |
|  2 | [m](./meta/sparsegpt.prototxt) | [ (SparseGPT) SparseGPT: Massive Language Models Can be Accurately Pruned in one-shot.](https://arxiv.org/pdf/2301.00774.pdf)                                                                                                                        | arXiv-2023         | [Pytorch](https://github.com/IST-DASLab/sparsegpt)   | [note](./notes/SparseGPT.md) |
|  3 | [m](./meta/2U5DXO7C.prototxt)  | [ (MVUE) Minimum Variance Unbiased N:M Sparsity for the Neural Gradients](https://openreview.net/pdf?id=vuD2xEtxZcj)                                                                                                                                 | ICLR-2023          |                                                      |                              |
|  4 | [m](./meta/OpenVINO.prototxt)  | [ (OpenVINO) Post-training deep neural network pruning via layer-wise calibration](https://openaccess.thecvf.com/content/ICCV2021W/LPCV/papers/Lazarevich_Post-Training_Deep_Neural_Network_Pruning_via_Layer-Wise_Calibration_ICCVW_2021_paper.pdf) | ICCV workshop-2021 |                                                      |                              |