import sys, re, json
from collections import Counter

# 使い方: python add_p75.py <入力 data.js> <出力 data.js> [<入力 index.html> <出力 index.html>]
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()

CAT = "口語表現（2）"
BL = "( &nbsp; &nbsp; &nbsp; )"
J = lambda x: json.dumps(x, ensure_ascii=False)
INS_SORT = "<small class='instruction-note'>次の語句を並び替えなさい。</small><br>"
INS_SORT_JP = "<small class='instruction-note'>日本文に合うように、次の語句を並び替えなさい。</small><br>"
INS_PARA = "<small class='instruction-note'>下線部とほぼ同じ意味を表すものを選びなさい。</small><br>"

def choice(no, q, ch, ans, audio, tr, ex, diff, school):
    assert ans in ch and len(ch) in (4, 5), no
    return ('{ page: 75, no: %s, category: %s, type: "4choice",\n'
            '    question: %s,\n'
            '    choices: [%s],\n'
            '    answer: %s, audioText: %s,\n'
            '    translation: %s,\n'
            '    explanation: %s,\n'
            '    difficulty: %s, school: %s  }') % (
        J(no), J(CAT), J(q), ", ".join(J(c) for c in ch), J(ans), J(audio), J(tr), J(ex), J(diff), J(school))

def sort(no, q, words, ans, audio, tr, ex, diff, school):
    assert Counter(" ".join(words).split()) == Counter(ans.split()), no
    assert len(q.split(BL)) - 1 == len(words), no
    return ('{ page: 75, no: %s, category: %s, type: "sort",\n'
            '    question: %s,\n'
            '    words: [%s],\n'
            '    answer: %s, audioText: %s,\n'
            '    translation: %s,\n'
            '    explanation: %s,\n'
            '    difficulty: %s, school: %s  }') % (
        J(no), J(CAT), J(q), ", ".join(J(w) for w in words), J(ans), J(audio), J(tr), J(ex), J(diff), J(school))

E = []
# ---------- 75-2 Why don’t you ～? / What do you say to ～ing? ----------
E.append(sort("2-1", INS_SORT + BL*7 + "?",
  ["the newspaper", "why", "or", "read", "you", "something", "don’t"],
  "why don’t you read the newspaper or something",
  "Why don’t you read the newspaper or something?",
  "新聞でも読んだらどうですか。",
  "Why don’t you ～? は「～してはどうですか」と相手に提案する表現で、後ろに動詞の原形を続けます。or something は「～か何か」という意味で、例を挙げてぼかす言い方です。したがって、Why don’t you read the newspaper or something? の語順になります。",
  "基礎", "龍谷大"))
E.append(choice("2-2", "Why don’t you go ( &nbsp; &nbsp; &nbsp; ) and I’ll join you later?",
  ["ahead", "further", "straight", "to"], "ahead",
  "Why don’t you go ahead and I’ll join you later?",
  "先に行ったらどう？私もあとから合流するよ。",
  "go ahead は「先に行く」という意味の熟語で、and I’ll join you later（あとで合流する）という内容に合います。Why don’t you ～? は「～してはどうですか」という提案の表現です。further は「さらに先へ」、straight は「まっすぐに」という意味で、「先に行く」の意味になりません。to は後ろに場所を表す語が必要です。※ Go ahead. は「どうぞ、お先に」と相手にすすめるときにも使います。",
  "基礎", "鹿児島国際大"))
E.append(choice("2-a", "( &nbsp; &nbsp; &nbsp; ) some coffee?",
  ["How do you say having", "How do you say to have", "What do you say to have", "What do you say to having"],
  "What do you say to having",
  "What do you say to having some coffee?",
  "コーヒーでもいかがですか。",
  "What do you say to ～ing? は「～してはどうですか、～はいかがですか」と提案する表現です。この to は不定詞の to ではなく前置詞なので、後ろは動名詞（having）になります。How do you say ～? は「～はどのように言いますか」と言い方をたずねる表現で、提案の意味になりません。",
  "標準", "立命館大"))
E.append(sort("2-b", INS_SORT_JP + "What " + BL*6 + " with me to Canada?<br><small>私と一緒にカナダ旅行はいかがですか。</small>",
  ["do", "a trip", "you", "making", "say", "to"],
  "do you say to making a trip",
  "What do you say to making a trip with me to Canada?",
  "私と一緒にカナダ旅行はいかがですか。",
  "What do you say to ～ing? は「～してはどうですか、～はいかがですか」と提案する表現です。この to は前置詞なので、後ろには動名詞（making）を置きます。make a trip は「旅行をする」という意味で、making a trip with me to Canada と続けます。したがって、What do you say to making a trip with me to Canada? の語順になります。",
  "標準", "東京家政大・改"))

# ---------- 75-7 would appreciate / Would it be all right if ～? ----------
E.append(choice("7-1", "I would ( &nbsp; &nbsp; &nbsp; ) it if you would deal with this matter urgently.",
  ["appeal", "appoint", "appreciate", "approach"], "appreciate",
  "I would appreciate it if you would deal with this matter urgently.",
  "この件を至急ご対応いただければ幸いです。",
  "I would appreciate it if you would ～. は「～していただけるとありがたいのですが」と、丁寧に依頼する表現です。appreciate は「～をありがたく思う」という意味で、it は後ろの if 節を指します。deal with ～ は「～を処理する、～に対応する」という意味の熟語です。appeal は「訴える」、appoint は「任命する」、approach は「近づく」という意味で、文意に合いません。",
  "基礎", "立命館大"))
E.append(choice("7-2", "It ( &nbsp; &nbsp; &nbsp; ) appreciated if you could reply to us as soon as possible.<br><small>お早めにご返信いただけましたら、ありがたく存じます。</small>",
  ["is", "will be", "would be", "must be"], "would be",
  "It would be appreciated if you could reply to us as soon as possible.",
  "お早めにご返信いただけましたら、ありがたく存じます。",
  "It would be appreciated if you could ～. は「～していただけるとありがたいのですが」と、丁寧に依頼する表現です。if 節に could があり、仮定法の形で控えめに依頼しているので、主節も would を使い、would be appreciated（ありがたく思われるでしょう）とします。is、will be、must be は、仮定法の形に合わず、依頼の表現として不自然です。",
  "基礎", ""))
E.append(choice("7-3", "A: ( &nbsp; &nbsp; &nbsp; ) all right if I came again some other time?<br>B: Of course. Just give me a call before you come.",
  ["Is it", "Was it", "Would it be", "Will it be"], "Would it be",
  "Would it be all right if I came again some other time?",
  "A：また別の機会に来てもよろしいですか。\nB：もちろんです。来る前に電話をください。",
  "Would it be all right if I ～? は「～してもかまいませんか」と、丁寧に許可を求める表現です。if 節の動詞が過去形（came）で、仮定法の形で控えめにたずねているので、主節は would を使います。Is it や Will it be は、このような丁寧な言い方になりません。Was it は過去のことをたずねる形で、文意に合いません。",
  "基礎", "センター試験"))
E.append(sort("7-4", INS_SORT_JP + "Would it " + BL*6 + " the window?<br><small>窓を開けてもかまいませんか。</small>",
  ["right", "if", "open", "all", "be", "I"],
  "be all right if I open",
  "Would it be all right if I open the window?",
  "窓を開けてもかまいませんか。",
  "Would it be all right if I ～? は「～してもかまいませんか」と、丁寧に許可を求める表現です。if 節の動詞は、必ずしも過去形とは限らず、この問題のように現在形（open）になることもあります。したがって、Would it be all right if I open the window? の語順になります。",
  "基礎", "鹿児島国際大"))
E.append(sort("7-5", INS_SORT + BL*6 + " here?",
  ["if I", "would", "all right", "be", "smoked", "it"],
  "would it be all right if I smoked",
  "Would it be all right if I smoked here?",
  "ここでたばこを吸ってもかまいませんか。",
  "Would it be all right if I ～? は「～してもかまいませんか」と、丁寧に許可を求める表現です。if 節の動詞に過去形（smoked）を使うと、控えめな言い方になります。したがって、Would it be all right if I smoked here? の語順になります。",
  "基礎", "名城大・改"))

# ---------- 75-9 Why not ----------
E.append(choice("9-1", "A: Shall we go?<br>B: ( &nbsp; &nbsp; &nbsp; ).",
  ["Certainly not", "Of course not", "Not at all", "Why not"], "Why not",
  "Why not.",
  "A：行きましょうか。\nB：そうしよう。",
  "Shall we ～? は「～しましょうか」と相手を誘う表現で、これに同意するときは Why not.（そうしよう、いいですね）と答えます。Certainly not と Of course not は「とんでもない、もちろん違う」と強く否定する言い方です。Not at all は「どういたしまして、少しも～ない」という意味で、いずれも誘いに同意する返事になりません。",
  "基礎", ""))
E.append(choice("9-a", "You have studied English for many years in Japan, so ( &nbsp; &nbsp; &nbsp; ) try to use it abroad?",
  ["why not", "what about", "whether or not", "how about"], "why not",
  "You have studied English for many years in Japan, so why not try to use it abroad?",
  "あなたは日本で何年も英語を勉強してきたのだから、海外でそれを使ってみてはどうですか。",
  "Why not ＋ 動詞の原形 ～? は「～してはどうですか」と提案する表現です。ここでは Why not try to ～? の形になります。what about と how about は、後ろに名詞や動名詞（～ing）を置く形なので、動詞の原形 try を続けられません。whether or not は「～かどうか」という意味で、提案の表現になりません。",
  "標準", "関西学院大"))

# ---------- 75-11 none of your business / concern ----------
E.append(choice("11", "It’s none of your ( &nbsp; &nbsp; &nbsp; ) who I want to go out with.",
  ["care", "concern", "interest", "knowledge", "regard"], "concern",
  "It’s none of your concern who I want to go out with.",
  "私が誰とつき合いたいかは、あなたには関係がない。",
  "none of your concern は「あなたには関係ない、あなたの知ったことではない」という意味の表現で、none of your business とほぼ同じ意味を表します。concern は「関心事、かかわり」という意味の名詞です。care、interest、knowledge、regard は、none of your のあとに置いても、この意味の慣用表現になりません。who 以下は、名詞節として「誰と～したいか」を表しています。go out with ～ は「～とつき合う」という意味の熟語です。",
  "基礎", "立教大"))

# ---------- 75-12 Now that ～ ----------
E.append(choice("12-1", "( &nbsp; &nbsp; &nbsp; ) that I’m a college student, I’ll read as many books as I can.",
  ["Since", "Now", "For", "Except"], "Now",
  "Now that I’m a college student, I’ll read as many books as I can.",
  "大学生になったのだから、できるだけ多くの本を読むつもりだ。",
  "Now that SV は「今や～なので、～した以上は」と理由を表す接続詞の働きをする表現です（that は省略できます）。空所の後ろに that があるので、Now が入ります。Since は理由を表しますが、後ろに that を置く形にはなりません。For と Except は、that 節を続けても、この文の理由を表しません。as many ～ as I can は「できるだけ多くの～」という意味です。",
  "基礎", "千葉工業大"))
E.append(choice("12-2", "( &nbsp; &nbsp; &nbsp; ) the war is over, there is a lot more food in the stores.",
  ["As far as", "Lest", "No sooner", "Now that"], "Now that",
  "Now that the war is over, there is a lot more food in the stores.",
  "戦争が終わったので、店には食料がずっと多く出回っている。",
  "Now that SV は「今や～なので、～した以上は」と理由を表す接続詞の働きをする表現です。As far as は「～する限り」という意味、Lest は「～しないように」という否定の意味を含む接続詞、No sooner は No sooner ～ than … の形で使う語で、いずれも文意に合いません。",
  "基礎", "創価大"))
E.append(choice("12-3", "( &nbsp; &nbsp; &nbsp; ) you’ve got a driver’s license, you may drive a car anytime.",
  ["Even if", "For fear that", "In order that", "Now that"], "Now that",
  "Now that you’ve got a driver’s license, you may drive a car anytime.",
  "運転免許を取ったのだから、いつでも車を運転してよい。",
  "Now that SV は「今や～なので、～した以上は」と理由を表す接続詞の働きをする表現です。Even if は「たとえ～でも」、For fear that は「～するといけないから」、In order that は「～するために」という意味で、いずれも文意に合いません。",
  "基礎", "日本女子大"))

# ---------- 75-14 So ＋ V ＋ S / fed up with ----------
E.append(choice("14-1", "My friend was absent from school yesterday, and ( &nbsp; &nbsp; &nbsp; ) was I.",
  ["neither", "either", "nor", "so"], "so",
  "My friend was absent from school yesterday, and so was I.",
  "友だちは昨日学校を休み、私もそうだった。",
  "「～もまたそうだ」は、肯定文を受けるときは ＜So ＋ 動詞 ＋ 主語＞ で表します。前の文が was absent の肯定文なので、so was I となります。neither と nor は否定文を受けるときに使い、either は否定文の文末で「～もまた（ない）」という意味で使うので、ここには入りません。",
  "基礎", "城西大"))
E.append(choice("14-2", "She likes rock music and ( &nbsp; &nbsp; &nbsp; ).",
  ["nor do I", "nor I do", "so do I", "so I do"], "so do I",
  "She likes rock music and so do I.",
  "彼女はロック音楽が好きだし、私もそうだ。",
  "先行する文は肯定文なので、so で受けます。「～もまたそうだ」は ＜So ＋ 助動詞（do など）＋ 主語＞ で表し、前の文の動詞 likes が一般動詞なので、do を使って so do I となります。nor は否定文を受けるときに使います。so I do のように倒置しない形は「そのとおりだ」という別の意味になります。",
  "基礎", "日本大"))
E.append(choice("14-3", "A: I usually go shopping downtown.<br>B: So ( &nbsp; &nbsp; &nbsp; ) my sister.",
  ["is", "will", "does", "was"], "does",
  "So does my sister.",
  "A：私はたいてい繁華街へ買い物に行きます。\nB：私の姉もそうです。",
  "「～もまたそうだ」は ＜So ＋ 助動詞 ＋ 主語＞ で表します。A の発言は go を使った一般動詞の現在形の肯定文なので、do を使って受けます。主語 my sister は三人称単数なので、does が入ります。is と was は be 動詞、will は未来を表す助動詞で、A の発言を受ける形になりません。",
  "基礎", "徳島文理大"))
E.append(choice("14-4", "I had a good time, and ( &nbsp; &nbsp; &nbsp; ).",
  ["did so Alice", "so Alice did", "did Alice so", "so did Alice"], "so did Alice",
  "I had a good time, and so did Alice.",
  "私は楽しい時間を過ごしたし、アリスもそうだった。",
  "「～もまたそうだ」は ＜So ＋ 助動詞 ＋ 主語＞ の語順で表します。前の文の動詞 had は一般動詞の過去形なので、did を使って受け、so did Alice となります。so Alice did のように倒置しない形や、did を前に置く did so Alice、did Alice so は、この意味を表す語順になりません。",
  "基礎", "関西外語大"))
E.append(choice("14-5", "A: He’s been waiting for her for a long time.<br>B: ( &nbsp; &nbsp; &nbsp; ).",
  ["Neither do I", "So have I", "So is he", "So he is"], "So have I",
  "So have I.",
  "A：彼は彼女をずっと待っているよ。\nB：私もだよ。",
  "A の発言の He’s は He has の短縮形で、has been waiting（現在完了進行形）の肯定文です。「私もそうだ」は ＜So ＋ 助動詞 ＋ 主語＞ で表すので、助動詞 have を使って So have I となります。Neither do I は否定文を受ける形です。So is he は主語が he で、「私も」という意味になりません。So he is は倒置していないので、「そのとおりだ」という別の意味になります。",
  "基礎", "東海大"))
E.append(choice("14-6", "Tom is having difficulty learning Japanese, and ( &nbsp; &nbsp; &nbsp; ).",
  ["also John does", "so is John", "as John is", "neither does John"], "so is John",
  "Tom is having difficulty learning Japanese, and so is John.",
  "トムは日本語を学ぶのに苦労しており、ジョンもそうだ。",
  "「～もまたそうだ」は ＜So ＋ 動詞 ＋ 主語＞ で表します。前の文は is having の形で、be 動詞を使った肯定文なので、be 動詞の is を使って so is John となります。neither は否定文を受けるときに使います。also John does と as John is は、この意味を表す語順になりません。have difficulty (in) ～ing は「～するのに苦労する」という意味です。",
  "基礎", "沖縄国際大"))
E.append(choice("14-7", "X: I forgot to do my homework.<br>Y: ( &nbsp; &nbsp; &nbsp; ).",
  ["Did I so.", "Neither did I.", "I didn’t either.", "So did I."], "So did I.",
  "So did I.",
  "X：宿題をするのを忘れた。\nY：私もだよ。",
  "X の発言は、一般動詞の過去形 forgot を使った肯定文です。「私もそうだ」は ＜So ＋ 助動詞 ＋ 主語＞ で表すので、did を使って So did I. となります。Neither did I. と I didn’t either. は否定文を受ける形で、Did I so. は、この意味を表す形になりません。",
  "基礎", "北海学園大"))
E.append(choice("14-8", "Mary is planning on attending the meeting this coming Sunday, and ( &nbsp; &nbsp; &nbsp; ).",
  ["so I am", "so am I", "so I do", "so do I"], "so am I",
  "Mary is planning on attending the meeting this coming Sunday, and so am I.",
  "メアリーは今度の日曜日の会議に出席する予定で、私もそうだ。",
  "前の文は is planning（be 動詞 ＋ 現在分詞）の肯定文なので、be 動詞を使って ＜So ＋ be 動詞 ＋ 主語＞ の形で受けます。主語が I なので、be 動詞は am となり、so am I が正解です。so I am は倒置していない形で、「そのとおりだ」という別の意味になります。so I do と so do I は、一般動詞を受ける形なので、ここには合いません。",
  "基礎", "東洋大"))
E.append(choice("14-9", "A: Mr. Anderson speaks Spanish.<br>B: ( &nbsp; &nbsp; &nbsp; ).",
  ["Does so his sister", "So does his sister", "Does his sister so", "His sister does so"], "So does his sister",
  "So does his sister.",
  "A：アンダーソンさんはスペイン語を話します。\nB：彼の妹もそうです。",
  "A の発言は、一般動詞 speaks の現在形の肯定文です。「～もまたそうだ」は ＜So ＋ 助動詞 ＋ 主語＞ で表すので、do を使って受け、主語 his sister が三人称単数なので So does his sister となります。Does so his sister と Does his sister so は、この意味を表す語順になりません。His sister does so は「彼の妹もそのようにする」という意味で、「～も」の意味を表せません。",
  "基礎", "法政大"))
E.append(choice("14-a", INS_PARA + "I am <u>fed up with</u> Tom.",
  ["given up", "arrested by", "tired of", "mixed with"], "tired of",
  "I am fed up with Tom.",
  "私はトムにうんざりしている。",
  "be fed up with ～ は「～にうんざりしている、あきあきしている」という意味の熟語で、be tired of ～ とほぼ同じ意味を表します。したがって、tired of が正解です。given up は「あきらめた」、arrested by は「～に逮捕された」、mixed with は「～と混ざった」という意味で、いずれも be fed up with ～ とは意味が違います。",
  "標準", "摂南大"))
E.append(choice("14-b", INS_PARA + "I am <u>fed up with</u> her.",
  ["sick and tired of", "involved with", "impressed with", "satisfied with"], "sick and tired of",
  "I am fed up with her.",
  "私は彼女にうんざりしている。",
  "be fed up with ～ は「～にうんざりしている、あきあきしている」という意味の熟語で、be sick and tired of ～ とほぼ同じ意味を表します。したがって、sick and tired of が正解です。involved with は「～にかかわって」、impressed with は「～に感銘を受けて」、satisfied with は「～に満足して」という意味で、いずれも be fed up with ～ とは意味が違います。",
  "標準", "成蹊大"))

# ---- 末尾（p73 の最後の問題の後ろ）に追加 ----
j = s.rindex('];')
k = s.rindex('}', 0, j)
last = s[s.rindex('{ page', 0, k):k]
assert last.startswith('{ page: 73'), "末尾の問題が p73 ではありません"
s = s[:k+1] + ",\n  " + ",\n  ".join(E) + s[k+1:]
open(dst, 'w', encoding='utf-8').write(s)
print("追加:", len(E), "問")

# ---- index.html にカテゴリのボタンを追加 ----
if len(sys.argv) >= 5:
    h = open(sys.argv[3], encoding='utf-8').read()
    key = "startCategory('口語表現（2）')"
    if key in h:
        print("index.html: 口語表現（2）のボタンは既にあります")
    else:
        m = re.search(r'^([ \t]*)<button class="btn-cat" onclick="startCategory\(\'口語表現（1）\'\)">口語表現（1）</button>\n', h, re.M)
        assert m, "口語表現（1）のボタンが見つかりません"
        new = m.group(0) + m.group(1) + '<button class="btn-cat" onclick="startCategory(\'口語表現（2）\')">口語表現（2）</button>\n'
        h = h[:m.start()] + new + h[m.end():]
        open(sys.argv[4], 'w', encoding='utf-8').write(h)
        print("index.html: ボタンを追加しました")
