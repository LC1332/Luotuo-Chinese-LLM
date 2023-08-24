<a name="BigTitle"></a>

[**English**](./README_EN.md) | [**中文**](https://github.com/LC1332/Luotuo-Chinese-LLM) | [快速上手](#quickstart) | [赞助](#sponsorship) | [赞助](#sponsorship) | [人员和贡献](#contributors) |  [相关项目](#related) | [骆驼读论文](https://github.com/LC1332/Luotuo-Paper-Reading)


# 骆驼(Luotuo): 开源中文大语言模型

骆驼(Luotuo)项目是由[冷子昂](https://blairleng.github.io) @ 商汤科技, [陈启源](https://qiyuan-chen.github.io/) @ 华中师范大学 以及 [李鲁鲁](https://github.com/LC1332) @ 商汤科技 发起的中文大语言模型开源项目，包含了一系列大语言模型、数据、管线和应用。

<p align="center">
  <img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/camel_back.png">
</p>

骆驼项目**不是**商汤科技的官方产品。

我们将项目命名为 骆驼 Luotuo (Camel) 主要是因为，Meta之前的项目LLaMA（驼马）和斯坦福之前的项目alpaca(羊驼)都属于偶蹄目-骆驼科（Artiodactyla-Camelidae）。而且骆驼科只有三个属，再不起这名字就来不及了。

## 项目重要更新 \[ [...](https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/data/previous_news.md) \]


[2023-07-12] 骆驼嵌入更新中模型 <a href="https://colab.research.google.com/github/LC1332/Luotuo-Text-Embedding/blob/main/notebook/Luotuo_Embedding_Visualization_Medium.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> 。我们后面将准备再训一个英语的嵌入模型。

[2023-06-07] 最近很多精力都在做 [Chat凉宫春日](https://github.com/LC1332/Chat-Haruhi-Suzumiya), 可以点这个体验 <a href="https://colab.research.google.com/github/LC1332/Prophet-Andrew-Ng/blob/main/prophet-code/haruhiLangChain.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> ,这个项目还在持续招人, [欢迎联系](https://github.com/LC1332/Prophet-Andrew-Ng/blob/main/Hiring.md)



## 子项目一览

<table style="table-layout:fixed; width: 100%;">
  <tr>
    <td style="text-align:center; width:50%;" width="50%">
      <b style="font-size:larger;"> Chat凉宫春日 </b>
      <br>
      <br>
      <a href="https://github.com/LC1332/Chat-Haruhi-Suzumiya"> 
        <img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/ProjHaruhi.jpg" alt="Contributor 2" height="250" width="100%">
        <br>
        Chat凉宫春日是模仿凉宫春日等一系列动漫人物，使用近似语气、个性和剧情聊天的语言模型方案
      </a>
    </td>
    <td style="text-align:center; width:50%;" width="50%">
      <b style="font-size:larger;"> 骆驼嵌入 </b>
      <br>
      <br>
      <a href="https://github.com/LC1332/Luotuo-Text-Embedding"> 
        <img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/ProjEmbedding.png" alt="Contributor 2" height="250" width="100%">
        <br>
        骆驼嵌入: Generative Text Embedding Model distilled from OpenAI API
      </a>
    </td>
  </tr>

  <tr>
    <td style="text-align:center; width:50%;" width="50%">
      <b style="font-size:larger;">  骆驼QA </b>
      <br>
      <br>
      <a href="https://github.com/LC1332/Luotuo-QA"> 
      <img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/ProjQA.png" alt="Contributor 1" height="250" width="100%">
      <br>
      骆驼QA: Better Conversational Question Answering Model with Answer Completion
      </a>
    </td>
    <td style="text-align:center; width:50%;">
      <b style="font-size:larger;"> 迷你骆驼 </b>
      <br>
      <a href="https://github.com/LC1332/Mini-Luotuo"> 
        <img src="https://github.com/LC1332/Mini-Luotuo/blob/main/images/ProjectIcon.png" alt="Contributor 2" height="250">
        <br>
        迷你骆驼:一系列蒸馏指令数据得到的中文语言模型
      </a>
    </td>
  </tr>

  <tr>
    <td style="text-align:center; width:50%;">
      <b style="font-size:larger;"> 丝绸之路 </b>
      <br>
      <a href="https://github.com/LC1332/Luotuo-Silk-Road"> 
        <img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/icon_silk_road.png" alt="Contributor 2" height="250">
        <br>
        丝绸之路: 构建中文大语言模型的数据基础
      </a>
    </td>
    <td style="text-align:center; width:50%;">
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
    <td style="text-align:center; width:50%;">
      <b style="font-size:larger;"> 骆驼先知 </b>
      <br>
      <a href="https://github.com/LC1332/Prophet-Andrew-Ng"> 
        <img src="https://github.com/LC1332/Prophet-Andrew-Ng/blob/main/figures/icon.png" alt="Contributor 2" height="250">
        <br>
        骆驼先知是模仿纪伯伦的《先知》进行哲学讨论。
        项目包含了Andrew Ng吴恩达Prompt工程的笔记和LangChain的笔记
      </a>
    </td>
  <td style="text-align:center; width:50%;">
      <b style="font-size:larger;"> 丝绸魔法书 </b>
      <br>
      <a href="https://github.com/LC1332/Luotuo-Silk-Magic-Book"> 
        <img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/icon_silk_scroll.png" alt="Contributor 2" height="250">
        <br>
        丝绸魔法书记录了大语言模型的一些魔法提示词(prompt)。
      </a>
    </td>
  </tr>

  <tr>
    <td style="text-align:center;">
      <b style="font-size:larger;"> 骆驼RPG </b>
      <br>
      <a href="https://github.com/LC1332/Chinese-generative-agents"> 
        <br>
        LuotuoRPG是斯坦福Generative Agents的中文版本尝试。
      </a>
    </td>
    <td style="text-align:center;">
      <b style="font-size:larger;"> 丫丫-MOSS </b>
      <br>
      <a href="https://github.com/qiyuan-chen/Yaya-Moss-Alpaca-LoRA"> 
        <br>
        丫丫是基于复旦MOSS的LoRA训练代码
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

[2023-05-20] 发布项目[迷你骆驼:一系列蒸馏指令数据得到的中文语言模型](https://github.com/LC1332/Mini-Luotuo),  3.5B小模型和测试代码 <a href="https://colab.research.google.com/github/LC1332/Mini-Luotuo/blob/main/3.5B_minimal.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>

[2023-05-06] 升级了数据集批量翻译的脚本 <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/improvedTranslation.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

[2023-04-27] 尝试翻译了一下斯坦福25个Agents生成的Generative Agents的工作。[代码仓库](https://github.com/LC1332/Chinese-generative-agents)，colab链接 <a href="https://colab.research.google.com/github/LC1332/Chinese-generative-agents/blob/main/notebook/Chinese_story_turbo.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

[2023-4-16] [骆驼嵌入](https://github.com/LC1332/Luotuo-Text-Embedding) 代码已经发布，可以用这个colab链接体验 <a href="https://colab.research.google.com/github/LC1332/Luotuo-Text-Embedding/blob/main/notebook/Luotuo_Embedding_Visualization.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  可支持文本可视化，聚类，模糊搜索等应用


<a name="quickstart"></a>

## 快速上手

|  | Colab链接 | 细节 |
| --- | --- | :--- |
|Chat凉宫春日(图文)|<a href="https://colab.research.google.com/github/LC1332/Chat-Haruhi-Suzumiya/blob/main/notebook/gradio_with_Image.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>| 能够根据台词搜索图片的gradio版本 |
|Chat凉宫春日|<a href="https://colab.research.google.com/github/LC1332/Prophet-Andrew-Ng/blob/main/prophet-code/haruhiLangChain.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>| 李鲁鲁最早开发的gradio Chat凉宫春日 |
| 骆驼先知 | <a href="https://colab.research.google.com/github/LC1332/Prophet-Andrew-Ng/blob/main/prophet-code/prophet-gradio.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> | 骆驼先知的Gradio交互版本 |
| 骆驼QA | <a href="https://colab.research.google.com/github/LC1332/Luotuo-QA/blob/main/colab/LuotuoQA_Gradio.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> | 骆驼QA的0.1模型，基于一段给定文本做问答 |
| 骆驼嵌入(小) | <a href="https://colab.research.google.com/github/LC1332/Luotuo-Text-Embedding/blob/main/notebook/Luotuo_Embedding_Visualization.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  | LuotuoBERT 文本可视化 聚类 搜索 |
| 驼铃C 文本摘要| <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/TuoLingC_evaluation_code.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> | 基于GLM-6B的文本摘要模型 |
| 批量翻译 | <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/improvedTranslation.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  | 利用GPT接口对数据集进行批量翻译 |
| 骆驼RPG | <a href="https://colab.research.google.com/github/LC1332/Chinese-generative-agents/blob/main/notebook/Chinese_story_turbo.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> | 一个斯坦福35个Agents生成的中文版 |
| 驼铃B Chat哈利波特 | - | [Chat哈利波特的初步汇报](https://github.com/LC1332/CamelBell-Chinese-LoRA/blob/main/data/HarryPotter/ShortReport.md) |
| 驼铃A | <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/TuoLing_evaluation_code.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> | 通过80条语料给GLM-6B简易洗脑 |
| 骆驼0.3 | <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/evaluation_code.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> | 骆驼0.3的验证代码 |
| 骆驼说 | <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/ChatLuotuo.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  | 一个用Gradio写的交互对话 |
| 骆驼说(GLM) | <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/ChatTuoling.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  | 中文文本摘要的Gradio交互界面 |




## 项目概览

让我来用时间顺序介绍整个骆驼项目的起源和发展。

在2023年3月20日，李鲁鲁老师实践了一下[Alpaca-Lora](https://github.com/tloen/alpaca-lora)的项目。

于是在3月21日的早晨，李鲁鲁在github上反查使用了LLaMATokenizer的代码，这个时候我们找到了[Japanese-Alpaca-LoRA](https://github.com/masa3141/japanese-alpaca-lora)项目。于是我们很快意识到，也可以用同样的方法尝试用中文去tuning LLaMA的模型。

于是在简短的讨论后，我们建立了Chinese-alpaca-lora这个项目，并且在当天就上传了对应的模型和demo。在这个时代，人们需要自己传播自己的工作，所以李鲁鲁在知乎写了第一篇关于骆驼的文章[【开源GPT】三位华人小哥开源中文语言模型“骆驼”，单卡即可完成训练部署，花费几百训练自己的中文聊天模型](https://zhuanlan.zhihu.com/p/615968438)

<table>
  <tr>
    <td width= "165"><img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/icon_luotuo.png" alt="Luotuo-Vanilla" width="160"></td>
    <td>
      <h2><a href="https://github.com/LC1332/Chinese-alpaca-lora"> Luotuo 骆驼 </a></h2>
      <p> Luotuo-Vanilla是骆驼项目的第一个github仓库, 它是在LLaMA-7B上进行微调的。骆驼项目的初始目标，是研究使用跨语言数据在进行微调时，大语言模型发生的相关现象。 </p>
    </td>
  </tr>
</table>

<details>
  <summary>详细描述</summary>

测试代码 <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/evaluation_code.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>

一个使用Gradio搭建的交互界面 <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/ChatLuotuo.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

我们还在完善骆驼1.0的训练数据和修复bug，并且在后续的版本中，我们将研究如何修复骆驼的Tokenizer。

骆驼0.3 的输出样例

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

这个项目很快在三天之内获得了100个stars。不过这个时候我们发现唐杰老师的研究组已经发布了ChatGLM，那个时候GLM还没有对应的tuning代码。

于是我们简单修改并且尝试了一个总结摘要的LoRA模型

<table>
  <tr>
    <td width= "165"><img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/icon_camelbell.png" alt="Luotuo-Vanilla" width="160"></td>
    <td>
      <h2><a href="https://github.com/LC1332/CamelBell-Chinese-LoRA"> Cambell 驼铃 </a></h2>
      <p> 如果你希望模型在中文上有更好的表现，建议使用 CamelBell(驼铃), 这个项目在中文基模型Chat-GLM-6B的基础上继续使用中文语料进行训练。 </p>
    </td>
  </tr>
</table>

<details>
  <summary> 详情 </summary>
  
在驼铃-B(CamelBell-B)中我们将训练一个[Chat哈利波特](https://github.com/LC1332/CamelBell-Chinese-LoRA/blob/main/data/HarryPotter/ShortReport.md)

CamelBell-B的输出样例

```
Instruction: 斯内普和伏地魔之间是什么关系?
Answer: 斯内普和伏地魔之间是非常复杂的关系。伏地魔是斯内普的雇主,他利用斯内普来执行他的计划。斯内普一开始是斯莱特林的学生,但他后来加入了伏地魔的阵营,成为了他的追随者。斯内普和伏地魔之间的关系非常紧张,他们互相对抗,但也有一些共同的利益。
```


CamelBell-C (驼铃-C)是一个中文文本摘要模型 <a href="https://colab.research.google.com/github/LC1332/Luotuo-Chinese-LLM/blob/main/notebook/TuoLingC_evaluation_code.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

CamelBell-C的输出样例

```
Instruction: 请帮我总结以下内容:
Input: 
北京时间2月13日凌晨,2023年ATP250达拉斯站男单决赛。中国球员吴易昺先输一盘后挽救4个赛点并兑现第5个冠军点,最终以6(4)-7/7-6(3)/7-6(12)逆转惊险击败赛会5号种子、美国大炮伊斯内尔,就此改写历史,成为公开赛年代首位夺得ATP巡回赛男单冠军的中国大陆球员,并创造中国大陆球员的男单最高排名!

第一盘比赛,吴易昺在第12局错过了一个盘点,并最终抢七惜败;第二盘则挽救一个赛点后抢七局3-0领先开局,且以7-6(3)扳回一盘;第三盘决胜盘,在关键的第9局15-40落后情况下凭借连续的高质量发球逆转保发,之后比赛再次进入抢七,抢七局依然胶着,吴易昺又挽救了3个赛点,并兑现了自己的第5个冠军点,就此锁定冠军!历史性一刻到来时,吴易昺瞬间躺倒在地。全场比赛,伊斯内尔轰出了44记Ace球,但最终在主场依然输给了吴易昺。

凭借具有突破意义的这一冠,吴易昺在本周入账250个积分和112125美元的冠军奖金,在周一最新一期的男单排名榜单上,创中国大陆男网历史新高排名—第58位。根据比赛计划,吴易昺原本要出战本周进行的ATP250德拉海滩站,不过在达拉斯夺冠后,吴易昺因身体疲劳退出本站赛事,他的签位由幸运落败者约翰森替代。

Answer: 男子网坛历史性一刻!中国小将吴易昺逆转击败赛会5号种子,成公开赛年代首个冠军。
```

</details>

当然，随着ChatGLM2的发布，有很多更成熟的ChatGLM2的tuning项目，所以驼铃项目就休眠了。

到这里时候，我们开始思考，一方面想要突破模型token长度的限制，一方面需要结合本地知识库对模型进行输出。所以这里有两个关键点，一个是embedding，一个是Closed QA的模型。所以我们启动了骆驼嵌入和骆驼QA两个项目

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

[【开源骆驼】我们蒸馏了OpenAI的特征，并用它分析了周杰伦的歌词，还打算复现360的Demo](https://zhuanlan.zhihu.com/p/622433896)


骆驼嵌入是一个非相关从业者关注比较少的项目。但是我们发现其实有很多的开发者在使用这个模型。LuotuoBert在huggingface的下载量一度达到了一个月一万三千多次。这显然不是我们自己开发的下载量能cover的。骆驼嵌入最近有胡婧训练了中模型，并且我们(陈舒年)打算再训一个英语的嵌入模型，这样可以做一些中英文的对齐。

和骆驼嵌入同步启动的项目是骆驼QA。原则上骆驼嵌入+骆驼QA就可以形成一个好的本地知识库问答。在实践中我们相当于也验证了训练一个closed QA模型能够产生更好的效果。并且在上个月我们做了骆驼QA-B数据集(by 罗钦雨)。

[【开源骆驼】骆驼团队发布，中文阅读理解模型，骆驼QA，可给定知识文本进行问答](https://zhuanlan.zhihu.com/p/624662198)

<table>
  <tr>
    <td width= "165"><img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/icon_QA.png" alt="Luotuo-Embedding" width="160"></td>
    <td>
      <h2><a href="https://github.com/LC1332/Luotuo-QA"> 骆驼QA </a></h2>
      <p> 骆驼QA是指给定一段特定的文本，用户针对文本中的内容，进行一个提问。语言模型试图理解文本中的内容，对用户的问题进行回答。 </p>
    </td>
  </tr>
</table>

不过这个项目最近进入休眠状态。一个很有价值事情是在Luotuo-QA-B数据集上重新finetune一个ChatGLM2，并且集成接入Langchain。应该会形成一个不错的本地知识库问答的系统。不过最近ChatHaruhi占用了李鲁鲁和冷子昂大多数的业余时间，所以这个事情就没人去lead了，如果你有能力和兴趣host这个项目，欢迎来联系我。


需要注意的是，除了语言模型和训练本身，语言模型的prompt也是在最近几年出现的一类新的问题，或者甚至可以说是一种新的范式。


<table>
  <tr>
    <td width= "165"><img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/icon_silk_scroll.png" alt="Luotuo-Vanilla" width="160"></td>
    <td>
      <h2><a href="https://github.com/LC1332/Luotuo-Silk-Magic-Book"> Silk Magic Book 丝绸魔法书 </a></h2>
      <p> 丝绸魔法书记录了大语言模型的一些魔法提示词(prompt)。我们希望有一天，骆驼项目自己训练的语言模型，也能适配很复杂任务的prompt。  </p>
    </td>
  </tr>
</table>

让李鲁鲁非常惊讶的是，ChatGPT等超大模型中，往往能适配一些“超级prompt”，这些超级prompt其实很接近ChatGPT等这些模型的能力边界，李鲁鲁把这些prompt统一记录在了丝绸魔法书这个项目中。[【骆驼杂谈】让文心一言回答知乎问题，他高兴地喊出了“谢邀”](https://zhuanlan.zhihu.com/p/619269433)

在这个时候李鲁鲁的学习习惯已经调整为，看到一个需要学习的项目就fork下来，然后进行翻译或者comments，形成自己的理解。这其实相比于过往读论文，再让其他人去跑代码的方法，要直接了许多。当然这也得益于colab和huggingFace这些快速开发工具的进展。我一直在构思一篇《这是一个发展越来越快的时代》，本来想在校庆前后写的，之后找个时间写吧。

比如在看Stanford的Generative Agents的工作的时候，我们就可以顺手fork这个项目，[https://github.com/LC1332/Chinese-generative-agents](https://github.com/LC1332/Chinese-generative-agents) 并且进行一些翻译，就可以得到自己的结果。得益于计算机公共的底层和库，这种学习方式是非常高效的。

[【开源骆驼】把斯坦福的25 ChatGPT玩游戏翻译成中文，佟湘玉与白展堂密谈了起来](https://zhuanlan.zhihu.com/p/625240760)

在这个时期（5月初前后），吴恩达也放出了Prompting Engineering的课程。这个时候李鲁鲁注意到DataWhale翻译了这个课程。于是就在DataWhale的基础上fork了自己的版本，形成了[骆驼先知](https://github.com/LC1332/Prophet-Andrew-Ng)并且进行了很多有趣的实践。

[【骆驼读论文】关于Andrew Ng的prompt工程课程的实践，为GPT编写更准确而多样的提示词](https://zhuanlan.zhihu.com/p/627134012)

<table>
  <tr>
    <td width= "165"><img src="https://github.com/LC1332/Prophet-Andrew-Ng/blob/main/figures/icon.png" alt="Luotuo-Embedding" width="160"></td>
    <td>
      <h2><a href="https://github.com/LC1332/Prophet-Andrew-Ng"> 骆驼先知 </a></h2>
      <p> 骆驼先知是模仿纪伯伦的《先知》进行哲学讨论。项目包含了李鲁鲁对于Prompt Engineering和LangChain的实践。 </p>
    </td>
  </tr>
</table>

骆驼先知其实是整个Prompt Engineering课程的作业之一。当然这个项目后来又叠加了LangChain相关的大量笔记，很多内容非常有启发性。当然整体还是先知更有趣一些，就用先知作为这个项目的名字了

[【开源骆驼】上完吴恩达的提示词课程，我们复现了纪伯伦的《先知》，并和他讨论了加班、夜店和996](https://zhuanlan.zhihu.com/p/627628201)

这其实是个很有意思的尝试，通过《先知》的26个故事，可以把先知的思想和价值观进行整体的复活。同样的思想能不能用到二次元人物中呢？于是李鲁鲁花一天半的时间，收集了凉宫春日38段语料。形成了凉宫春日的初步版本。

<table>
  <tr>
    <td width= "165"><img src="https://github.com/LC1332/Chat-Haruhi-Suzumiya/blob/main/figures/haruhi_suzumiya_bondage_rp.jpg" alt="Chat_haruhi" width="160"></td>
    <td>
      <h2><a href="https://github.com/LC1332/Chat-Haruhi-Suzumiya"> Chat凉宫春日 </a></h2>
      <p> Chat凉宫春日是模仿凉宫春日等一系列动漫人物，使用近似语气、个性和剧情聊天的语言模型。 </p>
    </td>
  </tr>
</table>

在儿童节前后DataWhale学习微信群的测试中，大家纷纷表示ChatHaruhi的效果很好。于是我们在DataWhale和高天学长的粉丝群进行了成员的招募。本着"Deadline就是生产力，所以更多Deadline,更多生产力"的原则。ChatHaruhi的工作组先后完成了DataWhale的作业(二等奖 top3)，中科院心理所的特定人格文本生成(二等奖 top3)和魔搭社区hackathon的比赛(二等奖 top3)。

[【骆驼开源】Chat凉宫春日，将京阿尼的人物带到现实](https://zhuanlan.zhihu.com/p/636381450)

虽然不知道为什么从来没有拿过第一，但显然拿第一并不是一件非常重要的事情。这个项目我们准备在扩充到30个人物之后，做补充实验并形成一个技术report挂到arxiv上。其实到Chat凉宫春日已经是一个比较成熟的语言模型项目，包含了完整的prompting、记忆库、数据生成和微调的流程。这个应该会形成垂直应用的语言模型的标准范式之一，我看到有人逛WAIC的截图里面还有人在教这个笔记。并且在7月初魔搭比赛的时候，我们已经验证了角色扮演这个任务可以被合理降解到7B规模的模型，这其实是一个很不错的结论。

所以研究每个垂直人物能够压缩到多小，也是一个很重要的任务。黄钟健实现的迷你骆驼，就是我们学习LaMini的一个项目。在这个项目中，我们在尝试训练3B，1B和300M等更多的小模型。

<table>
  <tr>
    <td width= "165"><img src="https://github.com/LC1332/Mini-Luotuo/blob/main/images/ProjectIcon.png" alt="Chat_haruhi" width="160"></td>
    <td>
      <h2><a href="https://github.com/LC1332/Mini-Luotuo">  迷你骆驼 </a></h2>
      <p> 迷你骆驼:一系列蒸馏指令数据得到的中文语言模型。 </p>
    </td>
  </tr>
</table>


所以，骆驼项目究竟是什么？骆驼应该是李鲁鲁等人发起的个人学习项目。在这个项目中，我们确实也发布了很多模型，比如骆驼Bert, 骆驼QA, 迷你骆驼等模型。同时我们也关注中文的数据集，形成了大量的配套数据集工作。从骆驼先知和Chat凉宫春日开始，我们也开始关注语言模型的整体管线和应用。

对于我们个人来说，一方面我们希望把过往在vision积累的经验，转移到语言模型上，并且形成一定的积累。并且我们通过一系列子项目，可以明白在每个任务上，投入多少的开发量，多少的数据和多少的计算资源，这个任务的性能才能进一步提升到什么样的水平。这样才会使得我们累积重要的经验，使得在未来操作更严肃的任务的时候，作出更准确的判断。在这个学习过程中，也能顺便产生一些对社区很有用的东西，比如LuotuoBert和haruhi这些工具。

当然Chat凉宫春日是一个有趣的转折点，从这个项目开始，我们意识到其实不一定要做一些“必做”的项目，而是可以做一些炫酷的项目，这些炫酷的项目和社区产生的互动，其实会更有趣，并且也是一个更真实的应用。就好像凉宫春日的故事本身一样，主角不满足于平淡的生活，带领着SOS团进行着一系列神奇的冒险。

我们认为愿意联系我们进行投入的同学都是highly motivated的。其实对于每个人来说，大语言模型都是一个非常全新的命题。即使是资深的研究者，也要放下很多固有认知，去结合新的东西和过往的知识去进行研究。这也是为什么李鲁鲁一大把年纪了还是会积极地进行paper reading和笔记的记录。我们之后打算装修一下人员的页面，把要寻找读博机会和工作机会的同学进行标识。今天先把子项目介绍写到这里。欢迎大家点击后面的赞助链接进行赞助！

<a name="sponsorship"></a>

## 赞助(Sponsorships)


Top 3 Sponsors

|Time    | Sponsor     | Amount |
| --- | --- | --- | 
| 2023/6/20| Xiuhan | 3000 |
| 2023/3/28 | 张** | 2000 |
| 2023/4/2等| Tand| 1580|


balance =  5293.03  now. Detailed balance see in [sponsorship_and_balance.md](data/Sponsorship_and_balance.md)

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
      黄泓森 维护了服务器和大量数据代码
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/28683036?v=4" alt="Contributor 5" height="150">
      <br>
      <b>胡婧 @ 华中师范大学</b>
      <br>
      胡婧 正在进一步维护骆驼嵌入
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/40827070?s=400&u=ab66832b0821cf43840ceba64a137da5089afe28&v=4" alt="Contributor 6" height="150">
      <br>
      <b>陈舒年 @ 杜克大学</b>
      <br>
      陈舒年 参与了骆驼嵌入等多个项目
    </td>
  </tr>

  <tr>
    <td>
      <img src="https://avatars.githubusercontent.com/u/34046462?s=400&u=fb9f92b791dcffb7c37d8f3f3d99eac38379c663&v=4" alt="Contributor 5" height="150">
      <br>
      <b>刘思诣 @ Upenn</b>
      <br>
      刘思诣 参与了骆驼嵌入项目
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/52043573?s=400&u=21a6a45547a06472457a7d852f1894825b9d7794&v=4" alt="Contributor 4" height="150">
      <br>
      <b>孙骜 @ 清华大学</b>
      <br>
      孙骜 训练了骆驼QA的英文模型
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/19383886?v=4" alt="Contributor 6" height="150">
      <br>
      <b> 黄钟健 @ 西安电子科大 </b>
      <br>
      黄钟健训练了迷你骆驼
    </td>
  </tr>

  <tr>
    <td>
      <img src="https://avatars.githubusercontent.com/u/24369614?v=4" alt="Contributor 5" height="150">
      <br>
      <b>廖健生 Jansen</b>
      <br>
      廖健生 训练了骆驼QA的模型
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/62985169?v=4" alt="Contributor 4" height="150">
      <br>
      <b>罗钦雨 @ JHU</b>
      <br>
      罗钦雨 发布了骆驼QA-B数据集
    </td>
    <td>
      <img src="https://github.com/LC1332/Luotuo-Chinese-LLM/blob/main/image/idle_image.png" alt="Contributor 6" height="150">
      <br>
      <b> 更多 </b>
      <br>
      更多同学招募中。。。
    </td>
  </tr>
</table>

<a name="endOfContributors"></a>


## Citation

Please cite the repo if you use the data or code in this repo.

```
@misc{luotuo,
  author={Ziang Leng, Qiyuan Chen and Cheng Li},
  title = {Luotuo: An Instruction-following Chinese Language model, LoRA tuning on LLaMA},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/LC1332/Luotuo-Chinese-LLM}},
}
```

[回到开头](#BigTitle)