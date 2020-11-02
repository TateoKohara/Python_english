import re
import random

source = '英単語_01.txt'

with open(source) as f:
  date = f.read()

#print(date)  
english_words = re.findall('[a-z]+', date)
#print(english_words)
ja = re.findall('\s.*\n', date)
#print(ja)

meanings = []
for word in ja:
  m = re.sub('\t|\n', '', word)
  meanings.append(m)
#print(meanings)
words_dict = dict(zip(english_words, meanings))
#print(words_dict)
#ここまで辞書を作成

#ここからテスト作成
n_tests = 50
n_questions = 50

for test_num in range(n_tests):

  with open('English_test_{:02d}.txt'.format(test_num + 1), 'w') as f:

    f.write('出席番号：\n'
    '名前：\n\n'
    '第{}回英単語テスト\n\n'.format(test_num + 1)
    )

    for question_num in range(n_questions):
      question_word = random.choice(english_words)
      try:
        correct_answer = words_dict[question_word]
      except KeyError:
        print('KeyError Exception')
      meanings_copy = meanings.copy()
      meanings_copy.remove(correct_answer)
      wrong_answers = random.sample(meanings_copy, 3)

      answer_options = [correct_answer] + wrong_answers

      random.shuffle(answer_options)

      f.write('問{}. {}\n\n'.format(question_num + 1, question_word))

      for i in range(4):
        f.write('{}. {}\n'.format(i + 1, answer_options[i]))
      f.write('\n\n')  




