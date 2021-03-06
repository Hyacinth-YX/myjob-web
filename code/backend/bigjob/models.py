from django.db import models


class Job(models.Model):
    jobName = models.CharField(verbose_name="工作名称", max_length=64)
    jobSubName = models.CharField(max_length=64, null=True)
    jobSalary = models.CharField(max_length=64, null=True)
    jobLimitExperience = models.CharField(max_length=64, null=True)
    jobLimitStudy = models.CharField(max_length=64, null=True)
    jobArea = models.CharField(max_length=64, null=True)
    companyName = models.CharField(max_length=64, null=True)
    jobIndustry = models.CharField(max_length=64, null=True)
    financialStatus = models.CharField(max_length=64, null=True)
    scale = models.CharField(max_length=64, null=True)
    companyLogo = models.CharField(max_length=256, null=True)
    bonus = models.CharField(max_length=64, null=True)
    jid = models.CharField(max_length=128)
    lid = models.CharField(max_length=128)
    jobDescription = models.TextField(null=True)

    def __str__(self) -> str:
        return self.jobName

    class Meta:
        db_table = "job"
        verbose_name_plural = "具体岗位"
        verbose_name = "具体岗位"


class BigJob(models.Model):
    jobCat = models.IntegerField(verbose_name='catid')
    jobName = models.CharField(verbose_name="工作名称", max_length=64)
    jobDesc = models.TextField(null=True)
    jobWork = models.TextField(null=True)
    bigJobImg = models.CharField(max_length=256, null=True)
    holland1 = models.CharField(max_length=1, null=True)
    holland2 = models.CharField(max_length=1, null=True)
    holland3 = models.CharField(max_length=1, null=True)
    subject1 = models.CharField(max_length=64, null=True)
    subject2 = models.CharField(max_length=64, null=True)

    def __str__(self) -> str:
        return self.jobName

    class Meta:
        db_table = "bigJob"
        verbose_name_plural = "职业大类"
        verbose_name = "职业大类"


class HollandQuestions:
    questions = ['强壮而敏捷的身体对我很重要。',
                 '我必须彻底地了解事情的真相。',
                 '我的心情受音乐、色彩和美丽事物的影响极大。',
                 '和他人的关系丰富了我的生命并使它有意义。',
                 '我自信会成功。',
                 '我做事必须有清楚的指引。',
                 '我擅长于自己制作、修理东西。',
                 '我可以花很长的时间去想通事情的道理。',
                 '我重视美丽的环境。',
                 '我愿意花时间帮别人解决个人危机。',
                 '我喜欢竞争。',
                 '我在开始一个计划前会花很多时间去计划。',
                 '我喜欢使用双手做事。',
                 '探索新构思使我满意。',
                 '我是寻求新方法来发挥我的创造力。',
                 '我认为能把自己的焦虑和别人分担是很重要的。',
                 '成为群体中的关键任务执行者，对我很重要。',
                 '我对于自己能重视工作中的所有细节感到骄傲。',
                 '我不在乎工作把手弄脏。',
                 '我认为教育是个发展及磨练脑力的终身学习过程。',
                 '我喜欢非正式的穿着，尝试新颜色和款式。',
                 '我常能体会到某人想要和他人沟通的需要。',
                 '我喜欢帮助别人不断改进。',
                 '我在决策时，通常不愿冒险。',
                 '我喜欢购买小零件，做成成品。',
                 '有时我长时间阅读，玩拼图游戏，冥想生命本质。',
                 '我有很强的想象力。',
                 '我喜欢帮助别人发挥天赋和才能。',
                 '我喜欢监督事情直至完工。',
                 '如果我面对一个新情景，会在事前做充分的准备。',
                 '我喜欢独立完成一项任务。',
                 '我渴望阅读或思考任何可以引发我好奇心的东西。',
                 '我喜欢尝试创新的概念。',
                 '如果我和别人摩擦，我会不断尝试化干戈为玉帛。',
                 '要成功就必须定高目标。',
                 '我喜欢为重大决策负责。',
                 '我喜欢直言不讳，不喜欢转弯抹角。',
                 '我在解决问题前，必须把问题进行彻底分析。',
                 '我喜欢重新布置我的环境，使他们与众不同。',
                 '我经常借着和别人交谈来解决自己的问题。',
                 '我常想起草一个计划，而由别人完成细节。',
                 '准时对我来说非常重要。',
                 '从事户外活动令我神清气爽。',
                 '我不断地问：为什么？',
                 '我喜欢自己的工作能够抒发我的情绪和感觉。',
                 '我喜欢帮助别人找可以和他人相互关注的办法。',
                 '能够参与重大决策是件令人兴奋的事情。',
                 '我经常保持清洁 , 喜欢有条不紊。',
                 '我喜欢周边环境简单而实际。',
                 '我会不断地思索一个问题，直到找出答案为止。',
                 '大自然的美深深地触动我的灵魂。',
                 '亲密的人际关系对我很重要。',
                 '升迁和进步对我极重要。',
                 '当我把每日工作计划好时，我会较有安全感。',
                 '我不害怕过重工作负荷，且知道工作的重点。',
                 '我喜欢能使我思考、给我新观念的书。',
                 '我希望能看到艺术表演、戏剧及好的电影。',
                 '我对别人的情绪低潮相当的敏感。',
                 '能影响别人使我感到兴奋。',
                 '当我答应一件事时，我会竭尽监督所有细节。',
                 '我希望粗重的肢体工作不会伤害任何人。',
                 '我希望能学习所有使我感兴趣的科目。',
                 '我希望能做些与众不同的事。',
                 '我对别人的困难乐于伸出援手。',
                 '我愿意冒一点险以求进步。',
                 '当我遵循成规时，我感到安全。',
                 '我选车时，最先注意的是好的引擎。',
                 '我喜欢能刺激我思考的话。',
                 '当我从事创造性的事时，我会忘掉一切旧经验。',
                 '我对社会上有许多人需要帮助感到关注。',
                 '说服别人依计划行事是件有趣的事情。',
                 '我擅长于检查细节。',
                 '我通常知道如何应付紧急事件。',
                 '阅读新发现的书事件令人兴奋的事情。',
                 '我喜欢美丽、不平凡的东西。',
                 '我经常关心孤独、不友善的人。',
                 '我喜欢讨价还价。',
                 '我花钱时小心翼翼。',
                 '我用运动来保持强壮的身体。',
                 '我经常对大自然的奥秘感到好奇。',
                 '尝试不平凡的新事物是件相当有趣的事情。',
                 '当别人像我诉说他的困难时，我是个好听众。',
                 '做事失败了，我会再接再厉。',
                 '我需要确切地知道别人对我的要求是什么。',
                 '我喜欢把东西拆开，看看能否修理他们。',
                 '我喜欢研读所有的事实，再有逻辑的做出决定。',
                 '没有美丽事物的生活，对我而言是不可思议的。',
                 '人们经常告诉我他们的问题。',
                 '我常能借着资讯网络和别人取得联系。',
                 '小心谨慎的完成一件事是件有成就感的事情。']
