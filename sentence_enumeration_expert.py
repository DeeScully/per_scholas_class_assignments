# The SEX will include 2 interactions with the user in order to serve 2 primary purposes: the user will be prompted to upload his/her .txt files, then given the option to alter the minimum amount of words required to be defined as a sentence.
# The primary functions are the visual representation of the average number of sentences and total number of sentences found on the user’s uploaded .txt file.

fname = input ('Input file path of the txt file you wish to be counted: ')
min_words_range = range(3, 6)
max_words_in_sentence = 8
punctuations = ('.', ',', ';', '!', '?')
words_count = 0
sentences_count = 0
invalid = True

while invalid:
    try:
        min_words_in_sentence = input('Please input "3" or "4" as the minimum number of words you want in a sentence.  Alternatively, you may press "Enter" to use the default value of "5"') or 5
        min_words_in_sentence = int(min_words_in_sentence)
    except:
        print('You did not input an integer.  Please try again.')
        continue

    if min_words_in_sentence not in min_words_range:
        print('Your number is outside the valid range.  Please try again.')
        continue

    invalid = False

def is_word(word):
    if len(word) >= 3:
        return True


def is_sentence(word_list):
    global min_words_in_sentence, max_words_in_sentence
    #print('is sentence word list is', word_list)

    if min_words_in_sentence <= len(word_list) <= max_words_in_sentence:
        return True


def counter(total_words, total_sentences):
    if total_sentences == 0:
        mean_sentences = 'undefined'
    else: mean_sentences = total_words / total_sentences

    if total_sentences == 1:
        print('There is %d sentence in your txt file and the average words for the sentence is %s.' %(total_sentences, mean_sentences))
    else: print('There are %d sentences in your txt file, and the average words of each sentence is %s.' %(total_sentences, mean_sentences))


def punctuation_index(text):
    min_index = len(text)

    for i in punctuations:
        if min_index > text.find(i) > 0:
            min_index = text.find(i)

    return min_index


with open(fname) as fh:
    text = fh.read()

text_chk = True
while text_chk:
    if len(text) > 0:
        min_index = punctuation_index(text)
        #print('min_index is', min_index)
        #print('len txt is', len(text))
        temp_text = text[:min_index]
        #print('text before splitting', temp_text)
        temp_list = temp_text.split()
        #print('list after splitting', temp_list)
        temp_word_list = list()

        for i in temp_list:
            if is_word(i):
                temp_word_list.append(i)
                #print('temp word list is', temp_word_list)
                words_count += 1
                #print('word count is', words_count)

        if is_sentence(temp_word_list):
            #print('temp word list is', temp_word_list)
            #print('this is a sentence')
            sentences_count += 1

        if min_index == len(text):
            if text[-1] not in punctuations and is_sentence(temp_word_list):
                sentences_count -= 1

            counter(words_count, sentences_count)
            text_chk = False

        else:
            text = text[min_index + 1:]
    else:
        counter(words_count, sentences_count)
        text_chk = False

input('Press enter to exit the program.')




