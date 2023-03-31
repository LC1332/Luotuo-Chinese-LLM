# 骆驼(Luotuo): Open Sourced Chinese Language Models

Project 骆驼(Luotuo) was founded by 冷子昂 @ 商汤科技, 陈启源 @ 华中师范大学 and 李鲁鲁 @ 商汤科技

( Notice: _[陈启源](https://qiyuan-chen.github.io/) is now pursuing a PhD position_)

<p align="center">
  <img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/WechatIMG13.png"  height="250">
</p>

This is NOT an official product of SenseTime

We named project in Luotuo(Camel) because both LLaMA and alpaca are all belongs to Artiodactyla-Camelidae(偶蹄目-骆驼科)

## News \[ [...](https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/data/previous_news.md) \]

[2023-3-31] New Project Page.

[2023-3-30] We released Chinese Summarization Model, CamelBell-C (驼铃-C), try in this <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/TuoLingC_evaluation_code.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>. More result see in [CamelBell-repo](https://github.com/LC1332/CamelBell-Chinese-LoRA).

[2023-3-27] We plan to train a [**ChatHarryPotter**](https://github.com/LC1332/CamelBell-Chinese-LoRA/blob/main/data/HarryPotter/ShortReport.md), we've just finished the prelimiary experiment and have ver. 0.1 model, but it did not meet our expectation, see this [report](https://github.com/LC1332/CamelBell-Chinese-LoRA/blob/main/data/HarryPotter/ShortReport.md), and we are pursuing **a Harry Potter enthusiast Pythoner to join**.


## A Quick Start

Evaluating our model on Colab at first, which we strongly recommended.

<table>

  <tr>
    <td width= "165"><img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/idle_image.png" alt="Luotuo-Vanilla" width="160"></td>
    <td>
      <h2><a href="https://github.com/LC1332/CamelBell-Chinese-LoRA"> Cambell 驼铃 </a></h2>
      <p> If you seeking a better performance on Chinese, check CamelBell(驼铃), which finetuned Chinese data on Chinese base model Chat-GLM-6B. </p>
    </td>
  </tr>
</table>

+ CamelBell-B (驼铃-B) will be [ChatHarryPotter](https://github.com/LC1332/CamelBell-Chinese-LoRA/blob/main/data/HarryPotter/ShortReport.md)

```
Instruction: 斯内普和伏地魔之间是什么关系?
Answer: 斯内普和伏地魔之间是非常复杂的关系。伏地魔是斯内普的雇主,他利用斯内普来执行他的计划。斯内普一开始是斯莱特林的学生,但他后来加入了伏地魔的阵营,成为了他的追随者。斯内普和伏地魔之间的关系非常紧张,他们互相对抗,但也有一些共同的利益。
```

+ CamelBell-C (驼铃-C) is a Chinese Text Summarization Model <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/TuoLingC_evaluation_code.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

```
Instruction: 请帮我总结以下内容:
Input: 
北京时间2月13日凌晨,2023年ATP250达拉斯站男单决赛。中国球员吴易昺先输一盘后挽救4个赛点并兑现第5个冠军点,最终以6(4)-7/7-6(3)/7-6(12)逆转惊险击败赛会5号种子、美国大炮伊斯内尔,就此改写历史,成为公开赛年代首位夺得ATP巡回赛男单冠军的中国大陆球员,并创造中国大陆球员的男单最高排名!

第一盘比赛,吴易昺在第12局错过了一个盘点,并最终抢七惜败;第二盘则挽救一个赛点后抢七局3-0领先开局,且以7-6(3)扳回一盘;第三盘决胜盘,在关键的第9局15-40落后情况下凭借连续的高质量发球逆转保发,之后比赛再次进入抢七,抢七局依然胶着,吴易昺又挽救了3个赛点,并兑现了自己的第5个冠军点,就此锁定冠军!历史性一刻到来时,吴易昺瞬间躺倒在地。全场比赛,伊斯内尔轰出了44记Ace球,但最终在主场依然输给了吴易昺。

凭借具有突破意义的这一冠,吴易昺在本周入账250个积分和112125美元的冠军奖金,在周一最新一期的男单排名榜单上,创中国大陆男网历史新高排名—第58位。根据比赛计划,吴易昺原本要出战本周进行的ATP250德拉海滩站,不过在达拉斯夺冠后,吴易昺因身体疲劳退出本站赛事,他的签位由幸运落败者约翰森替代。

Answer: 男子网坛历史性一刻!中国小将吴易昺逆转击败赛会5号种子,成公开赛年代首个冠军。
```



<table>
  <tr>
    <td width= "220"><img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/idle_image.png" alt="Luotuo-Vanilla" width="180"></td>
    <td>
      <h2><a href="https://github.com/LC1332/Chinese-alpaca-lora"> Luotuo 骆驼 </a></h2>
      <p> Luotuo-Vanilla is first repo in Project Luotuo, which finetuned Chinese on LLaMA-7B. The original purpose of Luotuo is to invesgating the effect that tuning trans-lingual data on a large language model. </p>
    </td>
  </tr>
</table>

+ Check Evaluation Code Here <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/evaluation_code.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>

+ An Interface Demo via Gradio Here <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/ChatLuotuo.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

+ Luotuo 1.0 is still in training, because distribute on local server taking us sometime, still many bugs need to be fix.

```
Input: 中国的首都在哪里？
Luotuo-Output: 中国的首都是北京。
```

```
Input: 华中师范大学在哪里
Luotuo-0.1-Output: 华中师范大学位于北京
Luotuo-0.3-Output: 华中师范大学在武汉市。
```


<table>
  <tr>
    <td width= "220"><img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/idle_image.png" alt="Luotuo-Vanilla" width="200"></td>
    <td>
      <h2><a href="https://github.com/LC1332/Chinese-alpaca-lora"> Silk Scroll 丝绸卷轴 </a></h2>
      <p> Silk Scroll  </p>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td width= "220"><img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/idle_image.png" alt="Luotuo-Vanilla" width="200"></td>
    <td>
      <h2><a href="https://github.com/LC1332/Chinese-alpaca-lora"> Silk Road 丝绸之路 </a></h2>
      <p> Silk Road  </p>
    </td>
  </tr>
</table>



## Trained Model

| Model Name | Training Data and Setting |
| --- | :--- |
| [luotuo-lora-7b-0.1](https://huggingface.co/qychen/luotuo-lora-7b-0.1/tree/main) | Trained on Translated alpaca 52k data |
| [luotuo-lora-7b-0.3](https://huggingface.co/silk-road/luotuo-lora-7b-0.3) | Trained on Translated alpaca 52k data + guanaco, 1 epoch |
| luotuo-lora-7b-0.9 | (In Plan) cleaned alpaca 52k + full guanaco |

luotuo-lora-7b-0.3 the performance seems have significant improvement than 0.1, even just after 1 epoch.

<p align="center">
  <img src="image/0.3result_1epoch.png">
</p>

But 1 epoch cost us 7 hours to train, which cost more than $10. We will keep continue tuning it later.

## Qualitative Result(0.3)

Evaluation code are now in notebook/evaluation_code.ipynb

### Good Examples

```
Input: 中国的首都在哪里？
Luotuo-Output: 中国的首都是北京。
```

```
Input: 麦当劳是哪个国家的？
Luotuo-Output: 美国。
```

```
Input: 2017年美国总统是谁
Luotuo-Output: 2017年美国总统是特朗普
```


```
Input: 华中师范大学在哪里
Luotuo-0.1-Output: 华中师范大学位于北京
Luotuo-0.3-Output: 华中师范大学在武汉市。
```

this example failed in 0.1

### Bad Examples

```
Input: 商汤科技是做什么的？
Luotuo-0.1-Output: 商汤科技是一种技术，它用于创建互联网应用程序和服务。
Luotuo-0.3-Output: 商汤科技是一种技术，它可以用于创建新的产品和服务，以增加产品和服务的吸引力。它可以用于创建新的产品和服务，以增加产品和服务的吸引力。它可以用于创建新的产品和服务，以增加产品和服务的吸引力。它可以用于创建新的产品和服务，以增加产品和服务的吸引力。它可以用于创建新的产品和服务，以增加产品和服务的吸引力。它可以用于创建新的产品和服务，以增加产品和服务的吸引力。它可以用于创建新的
```

```
Input: 猫和狗的关系是什么
Luotuo-Output: 猫和狗之间的关系是友好的。它们通常在一起休息或玩耍。猫和狗之间的关系通常很好，它们通常在一起休息或玩耍。猫和狗之间的关系通常很好，它们通常在一起休息或玩耍。猫和狗之间的关系通常很好，它们通常在一起休息或玩耍。猫和狗之间的关系通常很好，它们通常在一起休息或玩耍。猫和狗之间的关系通常很好，它们通常在一起休息或玩耍。猫和狗之间的关系通常
```

## Training

We have tuned a Chinese LLaMA model baed on [LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/), [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca), [Alpaca LoRA](https://github.com/tloen/alpaca-lora), [cabrita](https://github.com/22-hours/cabrita), [Japanese-Alpaca-LoRA](https://github.com/masa3141/japanese-alpaca-lora)

The training code in in cleaning, if you are in very hurry, check the Japanese project and simply change the json training data file name.

## Data

This is an inbuilding project

The training code only made a slightly change on the Japanese-Alpaca-LoRA

A. [0.1 version model](https://huggingface.co/qychen/luotuo-lora-7b-0.1/tree/main) was trained on translated data, which translate the [alpaca_data.json](https://github.com/tatsu-lab/stanford_alpaca/blob/main/alpaca_data.json) to Chinese using ChatGPT API.
We paid around US $30-45 to translate the full dataset to chinese. Translated data is available. ([trans_chinese_alpaca_data.json](data/trans_chinese_alpaca_data.json))

B. We are also plan to consider the data in [Guanaco](https://guanaco-model.github.io/) hikariming's [alpaca_chinese_dataset](https://github.com/hikariming/alpaca_chinese_dataset) and carbonz0‘s [alpaca-chinese-dataset](https://github.com/carbonz0/alpaca-chinese-dataset), may updated it into later version.

We plan to upload two different models A and B, because the provider of B claim the clean data will bring significant improvement.

## Sponsorships(赞助)

Top 3 Sponsors

| Time     | Sponsor     | Amount |
| --- | --- | --- | 
| 2023/3/28 | 张**      | 2000 |
| 2023/3/25 | [肖**]( https://github.com/mobe1978)  | 520 |
| 2023/3/24 | *潇      | 518    |

balance = 5792 now. Detailed balance see in [sponsorship_and_balance.md](data/Sponsorship_and_balance.md)

这原本是我们的一个作业项目，我们原本计划训练到1.0为止。但是社区的热情超过了我们的想象。如果您愿意赞助我们的项目，可以

扫描这个[二维码](https://s1.imagehub.cc/images/2023/03/23/fba44d198f0bb887089b4d8739363c0b.jpeg)

并且加这个[支付宝](https://s1.imagehub.cc/images/2023/03/23/b69e4e47759132dd3d4bbafa7bd602aa.jpeg)账号，留下您的姓名

项目的资金流向将被公开，所有的资金将被用于数据的标注，训练算力的购买或者后续周边产品的发放。数据和算力的捐献也会一同总结在sponsorship的表格中。备用链接 [二维码](image/sponser_QR_code.jpeg) , [支付宝](image/alipay_friend.jpeg)账号

This was originally an exercise project for us, and we originally planned to train until version 1.0. However, the enthusiasm of the community exceeded our expectations. If you are willing to sponsor our project, you can scan this [QR code](image/sponser_QR_code.jpeg)  and add [this Alipay account](image/alipay_friend.jpeg), leaving your name.

All funds will be used for data annotation, purchase of training computing power, or distribution of subsequent peripheral products.

## TODO and Be a Contributor

It seems that there are many follow-up tasks to be done after the basic version is completed. Many developers in the community have put forward more friendly suggestions, and I have put a longer TODO list in [TODO_list.md](data/TODO_list.md).

inbuilding project

- [X] translate alpaca json data into Chinese
- [X] finetuning with lora(model 0.1)
- [X] release 0.1 model (model A)
- [X] model to hugging face, GUI demo
- [X] train lora with more alpaca data(model 0.3)
- [ ] (In Processing) train lora with more alpaca data(model 0.9)
- [ ] clean training code
- [ ] write the second phase plan for Luotuo

We plan to use this Luotuo project as the git repository for the entire Chinese LLM project. After the completion of the original Luotuo: LLaMA-LoRA, it will be migrated to Luotuo-vanilla. The CamelBell, Loulan, Silk-Road and other derivative Chinese language model projects will gradually be added to the Luotuo project.

## Citation

Please cite the repo if you use the data or code in this repo.

```
@misc{alpaca,
  author={Ziang Leng, Qiyuan Chen and Cheng Li},
  title = {Luotuo: An Instruction-following Chinese Language model, LoRA tuning on LLaMA},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/LC1332/Luotuo-Chinese-LLM}},
}
```

## A Quick Start

| Colab Link |  | detail |
| --- | --- | :--- |
| CamelBell quick evaluation | <a href="https://colab.research.google.com/github/LC1332/CamelBell-Chinese-LoRA/blob/main/notebook/CamelBell_evaluation_code.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> | Tuoling specific Evaluation Code |
| A quick evaluation | <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/evaluation_code.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> | Evaluation code with standard HuggingFace pipeline |
| Bot with Interface | <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/ChatLuotuo.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  | Interactive Chatting Bot using Gradio |
| Training Code | To be released | Training code, run on colab |
| Data Translation  | <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/translate_json_data.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> | Translation alpaca.json into Chinese |
