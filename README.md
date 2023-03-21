# Luotuo: Chinese-alpaca-lora
A Chinese finetuned instruction LLaMA. Developed by 冷子昂 @ 商汤科技, 陈启源 @ 华中师范大学 and 李鲁鲁 @ 商汤科技
(email: chengli@sensetime.com)

This is NOT an official product of SenseTime

This project only made a slightly change on the Japanese-Alpaca-LoRA

## Data

This is an inbuilding project

A. We plan to tune a Chinese LLaMA model baed on [LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/), [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca), [Alpaca LoRA](https://github.com/tloen/alpaca-lora), [cabrita](https://github.com/22-hours/cabrita), [Japanese-Alpaca-LoRA](https://github.com/masa3141/japanese-alpaca-lora)

B. We are also plan to consider the data in hikariming's [alpaca_chinese_dataset](https://github.com/hikariming/alpaca_chinese_dataset) and carbonz0‘s [alpaca-chinese-dataset](https://github.com/carbonz0/alpaca-chinese-dataset), may updated it into later version. 

We plan to upload two different models A and B, because the provider of B claim the clean data will bring significant improvement.

## TODO

inbuilding project
- [x] (DONE) test translate script (test for 10 lines)
- [x] (DONE) buy openAI API
- [x] (DONE) translate alpaca json data
- [ ] (IN PROCESSING) finetuning with lora(model A)
- [ ] final test
- [ ] upload to git
- [ ] upload to huggingFace
- [ ] train lora with more alpaca data(model B)
- [ ] write colab example
- [ ] write colab + gradio example

## Citation 
If you find this project useful in your research, please consider citing:

```
@inproceedings{leng2023luotuo-ch-alpaca,
  title={Luotuo: Chinese-alpaca-lora},
  author={Ziang Len, Qiyuan Chen and Cheng Li},
  year={2023}
}
```

