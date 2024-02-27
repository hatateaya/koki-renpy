define r = Character('灵梦', color="#ff1b54")
define m = Character('魔理沙', color="#fff129")
define a = Character('爱丽丝', color="#ffd88f")
define s = Character('萃香', color="#ffa654")

label start:
    # 字幕来源 BV1dx411o78f (原:av32153770) ; BV1LW411r7R8 (弹幕字幕)
    # 音乐: 温暖的神社 (sm13581210)
    # 原作:【東方合同動画企画】魔理沙とアリスのクッキーKiss(蓮奈理緒 さん) (sm9720246)
    play music warmjinja
    scene bg hakurei
    show reimu happy
    r "啊~"
    r "今天也是好天气"
    show reimu surprise at center
    r "!!"
    show reimu surprise at right
    show marisa happy at center
    show alice happy at left
    ""
    show marisa surprise
    show alice surprise
    m "啊,灵梦.又在偷懒了吗?"
    show reimu resignedly
    r "休息中哦"
    show marisa remind
    m "今天一定是休息日啦"
    show alice remind
    a "那,明天呢?"
    m "神社倒闭之日"
    show reimu angry
    r "kora!!"
    show marisa happy
    show alice happy
    m "kia!"
    show reimu resignedly
    r "啊,你们两个关系还真是好呢"
    show alice remind
    a "对了对了,今天特地为灵梦带了土产来了哦"
    show reimu resignedly
    r "啊啦,谢谢.那么我去准备茶水"
    show marisa remind
    m "灵梦~请给我顶级茶叶!"
    show reimu resignedly
    r "好好...(9)号茶可以了吧?"
    show reimu normal
    show alice normal
    show marisa normal
    m "果然爱丽丝做的巧克力蛋糕很好吃啊"
    m "面团口感湿润而且不发粘,有种清爽的甜味"
    m "可可是用van houten做的吗?"
    show alice happy
    a "嘿嘿,谢谢啦魔理沙"
    show reimu happy
    r "真的很好吃哦"
    show reimu remind
    r "但是,做这个的一直都是爱丽丝呢"
    r "......魔理沙没有尝试做过吗?"
    m "诶?我也是做过的哦?"
    show alice question
    show reimu question
    a "诶呀?我有吃过魔理沙做的点心吗?"
    r "爱丽丝没吃过的话那不就谁也没吃过吗?"
    show marisa angry
    m "没这回事吧!?这之前应该是做过的daze!"
    show marisa regret
    m "你看啊,就是之前收到的情人节礼物的回...赠..."
    a "我有收到过吗?"
    m "啊..."
    r "我虽然也给了,但是没收到会赠呢~......虽然是义理的"
    m "啊啊啊啊啊啊啊啊啊!!我忘记了啊!"
    show alice surprise
    a "呜哇!等等,魔理沙!?"
    show marisa regret
    m "白色情人节!抱歉!!我忘记了!"
    show alice normal
    python:
        rpg.show()
    m "所以说爱丽丝!虽然很抱歉,但是能另外再稍微等我一下吗?"
    m "再等等的话应该会有魔理沙的超棒礼物,送给最先到的人!大概!"
    show reimu resignedly
    r "最先到的第一位...看来是没我的份呢"
    show alice happy
    show reimu angry
    m "灵梦就请坚强的活下去吧!"
    r "给我等下!!"
    show marisa normal
    m "那么诸君!先走一步!!"
    hide marisa
    show alice normal at left
    show reimu normal at right
    ""
    show reimu resignedly
    r "热恋中的少女的力量真是可怕呢~"
    show alice embarrassed
    a "哎!热恋什么的......哪有,哎呀!灵梦也真实的......笨蛋~"
    r "好啦好啦,多谢款待"
    show alice happy
    a "粗茶淡饭,不成敬意(点头)"
    show alice normal
    show reimu speaking
    r "啊......,但是没想到魔理沙居然忘了回赠呢"
    show alice embarrassed
    a "没关系的啦这种事.我只要和魔理沙在一起就能感到很幸福了"
    show alice happy
    show reimu resignedly
    r "好啦好啦,多谢款待"
    a "粗茶淡饭,不成敬意(点头)"
    a "......"
    show suika disawake at center
    s "灵梦~,是客人吗?"
    r "是爱丽丝哦"
    show alice happy
    show reimu happy
    show suika happy
    a "萃香,你好啊.可以的话尝尝这个怎么样?"
    s "炭烧墨鱼干?"
    show reimu angry
    r "是点心哦!你这酒鬼!"
    show alice happy
    show suika eating
    a "来,萃香*"
    show suika surprise_happy
    s "啊......好吃!!"
    show reimu resignedly
    r "因为是点心嘛"
    show suika happy
    show alice happy
    a "来!灵梦也"
    show reimu surprise
    r "哎!?哇,等....."
    show reimu surprise_happy
    r "(哈呜)......真好吃"
    show suika normal_happy
    show reimu happy
    show alice surprise
    r "那...爱丽丝也来 (喂)"
    show alice happy
    a "(哈呜)唔嗯!"
    show alice happy
    a "那,灵梦也再来一次~(笑)"
    show suika happy
    s "我也要喂灵梦吃~!"
    show reimu resignedly
    r "你们啊......"
    scene bg sky_turning
    "正弦运动魔理沙"
    "直线运动灵乌路空"
    scene bg lijiao_university
    "立教大学"
    "未公开画面....."
    return

init python:
    import rpg
