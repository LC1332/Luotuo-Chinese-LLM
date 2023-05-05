<a name="BigTitle"></a>

[**English**](./README_EN.md) | [**中文**](https://github.com/LC1332/Luotuo-Chinese-LLM) | [快速上手](#quickstart) | [赞助](#sponsorship) | [赞助](#sponsorship) | [人员和贡献](#contributors) |  [相关项目](#related) | [骆驼读论文](https://github.com/LC1332/Luotuo-Paper-Reading)


# 骆驼(Luotuo): 开源中文大语言模型

骆驼(Luotuo)项目是由[冷子昂](https://blairleng.github.io) @ 商汤科技, 陈启源 @ 华中师范大学 以及 李鲁鲁 @ 商汤科技 发起的中文大语言模型开源项目，包含了一系列语言模型。

( 注意: [陈启源](https://qiyuan-chen.github.io/) 正在寻找2024推免导师，欢迎联系 )

<p align="center">
  <img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/camel_back.png">
</p>

骆驼项目**不是**商汤科技的官方产品。

我们将项目命名为 骆驼 Luotuo (Camel) 主要是因为，Meta之前的项目LLaMA（驼马）和斯坦福之前的项目alpaca(羊驼)都属于偶蹄目-骆驼科（Artiodactyla-Camelidae）。而且骆驼科只有三个属，再不起这名字就来不及了。

## 项目重要更新 \[ [...](https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/data/previous_news.md) \]

[2023-04-27] 尝试翻译了一下斯坦福35个Agents生成的Generative Agents的工作。[代码仓库](https://github.com/LC1332/Chinese-generative-agents)，colab链接 <a href="https://colab.research.google.com/github/LC1332/Chinese-generative-agents/blob/main/notebook/Chinese_story_turbo.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## 子项目一览

<table>
  <tr>
    <td style="text-align:center;">
      <b style="font-size:larger;">  骆驼QA </b>
      <br>
      <br>
      <a href="https://github.com/LC1332/Luotuo-QA"> 
      <img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/ProjQA.png" alt="Contributor 1" height="250">
      <br>
      骆驼QA: Better Conversational Question Answering Model with Answer Completion
      </a>
    </td>
    <td style="text-align:center;">
      <b style="font-size:larger;"> 骆驼嵌入 </b>
      <br>
      <br>
      <a href="https://github.com/LC1332/Luotuo-Text-Embedding"> 
        <img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/ProjEmbedding.png" alt="Contributor 2" height="250">
        <br>
        骆驼嵌入: Generative Text Embedding Model distilled from OpenAI API
      </a>
    </td>
  </tr>

  <tr>
    <td style="text-align:center;">
      <b style="font-size:larger;"> 丫丫-MOSS </b>
      <br>
      <a href="https://github.com/qiyuan-chen/Yaya-Moss-Alpaca-LoRA"> 
        <img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/idle_image.png" alt="Contributor 2" height="250">
        <br>
        丫丫是基于复旦MOSS的LoRA训练代码
      </a>
    </td>
    <td style="text-align:center;">
      <b style="font-size:larger;"> Vanilla 骆驼 </b>
      <br>
      <a href="https://github.com/LC1332/Chinese-alpaca-lora"> 
        <img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/icon_luotuo.png" alt="Contributor 2" height="250">
        <br>
        骆驼: An Instruction-following Chinese Language model, LoRA tuning on LLaMA
      </a>
    </td>
  </tr>
  
  <tr>
    <td style="text-align:center;">
      <b style="font-size:larger;"> 骆驼大乱斗 </b>
      <br>
      <a href="https://github.com/LC1332/Luotuo-Chinese-LLM"> 
        骆驼大乱斗正在构建之中...
        <br>
        骆驼大乱斗: Generating Massive Content for a Text-based Fighting Game
      </a>
    </td>
    <td style="text-align:center;">
      <b style="font-size:larger;"> 骆驼CLIP </b>
      <br>
      <a href="https://github.com/LC1332/Luotuo-Chinese-LLM"> 
        骆驼CLIP正在构建之中...
        <br>
        骆驼CLIP: Aligning Existed CLIP model with Multiple Prior Leveraged
      </a>
    </td>
  </tr>

</table>



## 项目重要更新 \[ [...](https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/data/previous_news.md) \]

[2023-4-23] 我们在复旦开源的MOSS基础上实现了[丫丫](https://github.com/qiyuan-chen/Yaya-Moss-Alpaca-LoRA)，需要双卡A100运行和单卡A100的inference

[2023-4-16] [骆驼嵌入](https://github.com/LC1332/Luotuo-Text-Embedding) 代码已经发布，可以用这个colab链接体验 <a href="https://colab.research.google.com/github/LC1332/Luotuo-Text-Embedding/blob/main/notebook/Luotuo_Embedding_Visualization.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  可支持文本可视化，聚类，模糊搜索等应用

[2023-3-27] 我们计划训练一个[**Chat哈利波特**](https://github.com/LC1332/CamelBell-Chinese-LoRA/blob/main/data/HarryPotter/ShortReport.md), 我们仅仅完成了初步的实验并实现了0.1版本的模型, 不过模型的效果不及我们的预期, 可以查看[这份报告](https://github.com/LC1332/CamelBell-Chinese-LoRA/blob/main/data/HarryPotter/ShortReport.md), 我们想寻找一个 **哈利波特的狂热粉丝同时又是高质量的Python程序员** 来参与到项目中，可以联系我们。


<a name="quickstart"></a>

## 快速上手

|  | Colab链接 | 细节 |
| --- | --- | :--- |
| 骆驼QA | <a href="https://colab.research.google.com/github/LC1332/Luotuo-QA/blob/main/colab/LuotuoQA_Gradio.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> | 骆驼QA的0.1模型，基于一段给定文本做问答 |
| 骆驼嵌入(小) | <a href="https://colab.research.google.com/github/LC1332/Luotuo-Text-Embedding/blob/main/notebook/Luotuo_Embedding_Visualization.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  | LuotuoBERT 文本可视化 聚类 搜索 |
| 驼铃C 文本摘要| <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/TuoLingC_evaluation_code.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> | 基于GLM-6B的文本摘要模型 |
| 骆驼RPG | <a href="https://colab.research.google.com/github/LC1332/Chinese-generative-agents/blob/main/notebook/Chinese_story_turbo.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> | 一个斯坦福35个Agents生成的中文版 |
| 驼铃B Chat哈利波特 | - | [Chat哈利波特的初步汇报](https://github.com/LC1332/CamelBell-Chinese-LoRA/blob/main/data/HarryPotter/ShortReport.md) |
| 驼铃A | <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/TuoLing_evaluation_code.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> | 通过80条语料给GLM-6B简易洗脑 |
| 骆驼0.3 | <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/evaluation_code.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> | 骆驼0.3的验证代码 |
| 骆驼说 | <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/ChatLuotuo.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  | 一个用Gradio写的交互对话 |
| 骆驼说(GLM) | <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/ChatTuoling.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  | 中文文本摘要的Gradio交互界面 |




## 项目概览

我们强烈建议首先先在Colab测试我们的代码，再考虑本地部署。


<table>
  <tr>
    <td width= "165"><img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/icon_embedding.png" alt="Luotuo-Embedding" width="160"></td>
    <td>
      <h2><a href="https://github.com/LC1332/Luotuo-Text-Embedding"> Luotuo Embedding 骆驼嵌入 </a></h2>
      <p> 骆驼嵌入是一个文本嵌入模型，可以将长文本转化为1536维的向量，支持文本可视化、搜索、聚类、内容审核等下游业务。 </p>
    </td>
  </tr>
</table>

骆驼嵌入是我们从OpenAI蒸馏特征得到的BERT的文本嵌入模型。<a href="https://colab.research.google.com/github/LC1332/Luotuo-Text-Embedding/blob/main/notebook/Luotuo_Embedding_Visualization.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> 

<table>
  <tr>
    <td width= "165"><img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/icon_camelbell.png" alt="Luotuo-Vanilla" width="160"></td>
    <td>
      <h2><a href="https://github.com/LC1332/CamelBell-Chinese-LoRA"> Cambell 驼铃 </a></h2>
      <p> 如果你希望模型在中文上有更好的表现，建议使用 CamelBell(驼铃), 这个项目在中文基模型Chat-GLM-6B的基础上继续使用中文语料进行训练。 </p>
    </td>
  </tr>
</table>

在驼铃-B(CamelBell-B)中我们将训练一个[Chat哈利波特](https://github.com/LC1332/CamelBell-Chinese-LoRA/blob/main/data/HarryPotter/ShortReport.md)


<details>
  <summary>CamelBell-B的输出样例 (点我) </summary>

```
Instruction: 斯内普和伏地魔之间是什么关系?
Answer: 斯内普和伏地魔之间是非常复杂的关系。伏地魔是斯内普的雇主,他利用斯内普来执行他的计划。斯内普一开始是斯莱特林的学生,但他后来加入了伏地魔的阵营,成为了他的追随者。斯内普和伏地魔之间的关系非常紧张,他们互相对抗,但也有一些共同的利益。
```

</details>



CamelBell-C (驼铃-C)是一个中文文本摘要模型 <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/TuoLingC_evaluation_code.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>


<details>
  <summary>CamelBell-C的输出样例 (点我)</summary>

```
Instruction: 请帮我总结以下内容:
Input: 
北京时间2月13日凌晨,2023年ATP250达拉斯站男单决赛。中国球员吴易昺先输一盘后挽救4个赛点并兑现第5个冠军点,最终以6(4)-7/7-6(3)/7-6(12)逆转惊险击败赛会5号种子、美国大炮伊斯内尔,就此改写历史,成为公开赛年代首位夺得ATP巡回赛男单冠军的中国大陆球员,并创造中国大陆球员的男单最高排名!

第一盘比赛,吴易昺在第12局错过了一个盘点,并最终抢七惜败;第二盘则挽救一个赛点后抢七局3-0领先开局,且以7-6(3)扳回一盘;第三盘决胜盘,在关键的第9局15-40落后情况下凭借连续的高质量发球逆转保发,之后比赛再次进入抢七,抢七局依然胶着,吴易昺又挽救了3个赛点,并兑现了自己的第5个冠军点,就此锁定冠军!历史性一刻到来时,吴易昺瞬间躺倒在地。全场比赛,伊斯内尔轰出了44记Ace球,但最终在主场依然输给了吴易昺。

凭借具有突破意义的这一冠,吴易昺在本周入账250个积分和112125美元的冠军奖金,在周一最新一期的男单排名榜单上,创中国大陆男网历史新高排名—第58位。根据比赛计划,吴易昺原本要出战本周进行的ATP250德拉海滩站,不过在达拉斯夺冠后,吴易昺因身体疲劳退出本站赛事,他的签位由幸运落败者约翰森替代。

Answer: 男子网坛历史性一刻!中国小将吴易昺逆转击败赛会5号种子,成公开赛年代首个冠军。
```

</details>



<table>
  <tr>
    <td width= "165"><img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/icon_luotuo.png" alt="Luotuo-Vanilla" width="160"></td>
    <td>
      <h2><a href="https://github.com/LC1332/Chinese-alpaca-lora"> Luotuo 骆驼 </a></h2>
      <p> Luotuo-Vanilla是骆驼项目的第一个github仓库, 它是在LLaMA-7B上进行微调的。骆驼项目的初始目标，是研究使用跨语言数据在进行微调时，大语言模型发生的相关现象。 </p>
    </td>
  </tr>
</table>

测试代码 <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/evaluation_code.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>

一个使用Gradio搭建的交互界面 <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/ChatLuotuo.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

我们还在完善骆驼1.0的训练数据和修复bug，并且在后续的版本中，我们将研究如何修复骆驼的Tokenizer。



<details>
  <summary>骆驼0.3 的输出样例 (点我)</summary>

```
Input: 中国的首都在哪里？
Luotuo-Output: 中国的首都是北京。
```

```
Input: 华中师范大学在哪里
Luotuo-0.1-Output: 华中师范大学位于北京
Luotuo-0.3-Output: 华中师范大学在武汉市。
```

</details>


<table>
  <tr>
    <td width= "165"><img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/idle_image.png" alt="Luotuo-Paper-Reading" width="160"></td>
    <td>
      <h2><a href="https://github.com/LC1332/Luotuo-Paper-Reading"> Paper Reading 骆驼读论文 </a></h2>
      <p> 在构建骆驼项目中，阅读的一些关于大语言模型，或者其他科研进展的论文 </p>
    </td>
  </tr>
</table>



<table>
  <tr>
    <td width= "165"><img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/icon_silk_scroll.png" alt="Luotuo-Vanilla" width="160"></td>
    <td>
      <h2><a href="https://github.com/LC1332/Luotuo-Silk-Magic-Book"> Silk Magic Book 丝绸魔法书 </a></h2>
      <p> 丝绸魔法书记录了大语言模型的一些魔法提示词(prompt)。我们希望有一天，骆驼项目自己训练的语言模型，也能适配很复杂任务的prompt。  </p>
    </td>
  </tr>
</table>



<table>
  <tr>
    <td width= "165"><img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/icon_silk_road.png" alt="Luotuo-Vanilla" width="160"></td>
    <td>
      <h2><a href="https://github.com/LC1332/Chinese-alpaca-lora"> Silk Road 丝绸之路 </a></h2>
      <p> Silk Road (丝绸之路) will be the model bank of project Luotuo. </p>
    </td>
  </tr>
</table>


<a name="sponsorship"></a>

## 赞助(Sponsorships)

Top 3 Sponsors

|Time    | Sponsor     | Amount |
| --- | --- | --- | 
| 2023/3/28 | 张** | 2000 |
| 2023/4/6 | 孙** | 1024|
| 2023/4/23| 孙*| 1000| 

balance =  5187  now. Detailed balance see in [sponsorship_and_balance.md](data/Sponsorship_and_balance.md)

这原本是我们的一个作业项目，我们原本计划训练到1.0为止。但是社区的热情超过了我们的想象。如果您愿意赞助我们的项目，可以

扫描这个[二维码](https://s1.imagehub.cc/images/2023/03/23/fba44d198f0bb887089b4d8739363c0b.jpeg)

并且加这个[支付宝](https://s1.imagehub.cc/images/2023/03/23/b69e4e47759132dd3d4bbafa7bd602aa.jpeg)账号，留下您的姓名

项目的资金流向将被公开，所有的资金将被用于数据的标注，训练算力的购买或者后续周边产品的发放。数据和算力的捐献也会一同总结在sponsorship的表格中。备用链接 [二维码](image/sponser_QR_code.jpeg) , [支付宝](image/alipay_friend.jpeg)账号

This was originally an exercise project for us, and we originally planned to train until version 1.0. However, the enthusiasm of the community exceeded our expectations. If you are willing to sponsor our project, you can scan this [QR code](image/sponser_QR_code.jpeg)  and add [this Alipay account](image/alipay_friend.jpeg), leaving your name.

All funds will be used for data annotation, purchase of training computing power, or distribution of subsequent peripheral products.

<a name="related"></a>

## 相关项目

我们计划在这里增加一个表格，列出所有我们已经关联，和正在following的开源项目列表。同时，非常感谢这些项目的作者对开源社区的贡献。

[太长不看](#contributors)

| 模型与训练 | 详情 |
| --- | --- |
| [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B) | ChatGLM-6B 是清华唐杰老师实验室释放出来的中文大语言(小)模型 |
| [ptuning-v2](https://github.com/THUDM/ChatGLM-6B/tree/main/ptuning) | ptuning-v2是清华唐杰老师实验室发布对GLM的一种微调方法，实现了他们本身发布的p-tuning-v2的论文的方法 |
|[GLM-Tuning](https://github.com/mymusise/ChatGLM-Tuning) | <a href="https://colab.research.google.com/github/mymusise/ChatGLM-Tuning/blob/master/examples/finetune.ipynb"><img alt="Build" src="https://colab.research.google.com/assets/colab-badge.svg"></a> 这是[Chengxi Guo](https://github.com/mymusise)等同学实现的GLM微调，最新的版本中同时支持了LoRA和p-tuning |
|[Alpaca](https://github.com/tatsu-lab/stanford_alpaca) | Alpaca是斯坦福在LLaMA上微调对话指令的项目，是万恶之源 |
|[Alpaca-LoRA](https://github.com/tloen/alpaca-lora) | 这个项目开启了LLaMA模型上的LoRA微调，万恶之源2 |
|[Alpaca-ChToken](https://github.com/ymcui/Chinese-LLaMA-Alpaca) | 复旦的Yiming Cui和Ziqing Yang修复了Alpaca的中文token问题，在原来的LLaMA英文token边上并了一个中文的token，我们想把这个项目整合到整体训练里，还没做完 |
|[BELLE-7B](https://github.com/LianjiaTech/BELLE)| [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LianjiaTech/BELLE/blob/main/notebook/BELLE_INFER_COLAB.ipynb) BELLE是贝壳(链家)放出来的中文大模型，我们之后会尝试在这上面做微调。在一个合适的定量benchmark建立以后，我们会对比各个单卡大模型之间的性能。|
|[RWKV-LM](https://github.com/BlinkDL/RWKV-LM)|RWKV也是一套语言模型的训练架构|
|[Baize-7B](https://github.com/project-baize/baize-chatbot)|白泽是做连续对话的，他收集语料的方法很有意思，之后我们要看一下，但是白泽是在LLaMA上训练的，所以会遇到中文的问题，用到中文要换基模型。 |
|[Vicuna](https://github.com/lm-sys/FastChat)|同时有7B和13B，支持中文的模型，这个应该挺厉害的，而且13B用Int4能够压缩到colab使用（但是不知道int4训练会不会出事儿），之后也要试一下|
|[DeepSpeed](https://github.com/microsoft/DeepSpeed/tree/master/blogs/deepspeed-chat/chinese) | 微软开源的一个快速训练RLHF和全局finetune的一个框架 |
|[Phoenix](https://github.com/FreedomIntelligence/LLMZoo)| 港中文深圳的老师同学们发布的Phoenix模型，拥有宽松，支持商业的开源协议，我们之后想有些模型也在这上面训练，另外感谢cite我们🙏|
|[中文OpenInstruct](https://github.com/flagopen/flaginstruct)|北京智源老师们准备开源出来的数据集，另外感谢cite我们!|

| 数据 | 详情 |
| --- | --- |
| [Guanaco](https://huggingface.co/datasets/JosephusCheung/GuanacoDataset) | Guanaco是JosephusCheung制作的一套指令调优的数据集，在骆驼0.3以上版本的模型中我们使用了这个数据。 |
| [CNewSum](https://dqwang122.github.io/projects/CNewSum/) | CNewSum是字节与UCSB发布的中文摘要数据集，我们在驼铃-C模型中使用了这个数据集 |
| [Coco-CN](https://github.com/li-xirong/coco-cn) | 这是中国人民大学的li-xirong等翻译的部分Coco数据集，**骆驼团队正在准备用GPT翻译完整的Coco,如果你也准备翻译，可以联系我们，避免重复花钱** |
| [CoQA](https://stanfordnlp.github.io/coqa/) | 基于一段文字，然后问答，是个很重要的任务。陈丹琦大佬参与做的CoQA数据集，**骆驼团队正在准备用GPT增广和翻译完整的CoQA,如果你也准备翻译，可以联系我们，避免重复花钱** |


<a name="contributors"></a>

## 贡献者(Contributors)

我们会把每个贡献者的贡献记录在[contributions.md](https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/data/contributions.md)，包括每个项目每个成员的具体任务分配和贡献。

这里的表格仅列出每个人的主要贡献，更具体的内容请参考contributions.md

[太长不看](#endOfContributors)

<table>
  <tr>
    <td>
      <img src="https://avatars.githubusercontent.com/u/5266090?v=4" alt="Contributor 1" height="150">
      <br>
      <b> 李鲁鲁 @ 商汤科技 </b>
      <br>
      李鲁鲁 是骆驼项目的发起人之一
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/25675774?v=4" alt="Contributor 2" height="150">
      <br>
      <b>冷子昂 @ 商汤科技</b>
      <br>
      冷子昂 是骆驼项目的发起人之一
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/72334646?v=4" alt="Contributor 3" height="150">
      <br>
      <b>陈启源 @ 华中师范大学 </b>
      <br>
      陈启源 是骆驼项目的发起人之一
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://avatars.githubusercontent.com/u/45280500" alt="Contributor 4" height="150">
      <br>
      <b>黄泓森 @ 华中师范大学</b>
      <br>
      黄泓森 维护了docker和项目环境
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/28683036?v=4" alt="Contributor 5" height="150">
      <br>
      <b>胡婧 @ 华中师范大学</b>
      <br>
      胡婧 正在参与一些后续项目
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/40827070?s=400&u=ab66832b0821cf43840ceba64a137da5089afe28&v=4" alt="Contributor 6" height="150">
      <br>
      <b>陈舒年 @ 杜克大学</b>
      <br>
      陈舒年 正在参与ChatYisheng等
    </td>
  </tr>

  <tr>
    <td>
      <img src="https://avatars.githubusercontent.com/u/34046462?s=400&u=fb9f92b791dcffb7c37d8f3f3d99eac38379c663&v=4" alt="Contributor 5" height="150">
      <br>
      <b>刘思诣 @ Upenn</b>
      <br>
      刘思诣 正在参与一些后续项目
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/52043573?s=400&u=21a6a45547a06472457a7d852f1894825b9d7794&v=4" alt="Contributor 4" height="150">
      <br>
      <b>孙骜 @ 清华大学</b>
      <br>
      孙骜 正在参与中文QA等工作
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/19383886?v=4" alt="Contributor 6" height="150">
      <br>
      <b> 黄钟健 @ 西安电子科大 </b>
      <br>
      黄钟健编写了Chat驼铃
    </td>
  </tr>
</table>

<a name="endOfContributors"></a>


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

[回到开头](#BigTitle)

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

## A Quick Start

| Colab Link |  | detail |
| --- | --- | :--- |
| CamelBell quick evaluation | <a href="https://colab.research.google.com/github/LC1332/CamelBell-Chinese-LoRA/blob/main/notebook/CamelBell_evaluation_code.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> | Tuoling specific Evaluation Code |
| A quick evaluation | <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/evaluation_code.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> | Evaluation code with standard HuggingFace pipeline |
| Bot with Interface | <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/ChatLuotuo.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  | Interactive Chatting Bot using Gradio |
| Training Code | To be released | Training code, run on colab |
| Data Translation  | <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/translate_json_data.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> | Translation alpaca.json into Chinese |
