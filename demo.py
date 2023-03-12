import time
import numpy as np

def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(.05)
    print()

print("""\
                _ ___                /^^\ /^\  /^^\_
    _          _@)@) \            ,,/ '` ~ `'~~ ', `\.
  _/o\_ _ _ _/~`.`...'~\        ./~~..,'`','',.,' '  ~:
 / `,'.~,~.~  .   , . , ~|,   ,/ .,' , ,. .. ,,.   `,  ~\_
( ' _' _ '_` _  '  .    , `\_/ .' ..' '  `  `   `..  `,   \_
 ~V~ V~ V~ V~ ~\ `   ' .  '    , ' .,.,''`.,.''`.,.``. ',   \_
  _/\ /\ /\ /\_/, . ' ,   `_/~\_ .' .,. ,, , _/~\_ `. `. '.,  \_
 < ~ ~ '~`'~'`, .,  .   `_: ::: \_ '      `_/ ::: \_ `.,' . ',  \_
  \ ' `_  '`_    _    ',/ _::_::_ \ _    _/ _::_::_ \   `.,'.,`., \-,-,-,_,_,
   `'~~ `'~~ `'~~ `'~~  \(_)(_)(_)/  `~~' \(_)(_)(_)/ ~'`\_.._,._,'_;_;_;_;_;
""")

slow_print('Welcome to the Demo of AlphaEncoder Project!')
slow_print('This is a project that encodes and decodes text using the Enigma algorithm in order do encode and decode a message.')
slow_print('It uses matrixes and permutations to encode and decode the message.')
slow_print('Authors: Thomas Chiari Ciocchetti de Souza and Marcelo Rabello Barranco')
slow_print('Version: 1.0')
print("")

slow_print("To start, we need to get the message to be encoded.")
slow_print("Please, type the message you want to encode. Please, only use alphabet letters, spaces and numbers.")
message = input("Message: ")
print("")

slow_print("Now, we will generate the keys to encode the message.")

P = np.random.permutation(np.eye(37))
E = np.random.permutation(np.eye(37))

slow_print("The keys are:")
print("P = ")
print(P)
print("E = ")
print(E)

slow_print("In this case, the keys will be randomly generated, but you can use your own keys using the AlphaEncoder API.")
slow_print("Note that the keys are permutations of the identity matrix.")
slow_print("Now, we will encode the message.")
slow_print("For that, we will call the Enigma function from the AlphaEncoder module, and use the permutation matrixes.")

from AlphaEncrypter import enigma, de_enigma

encoded_message = enigma(message, P, E)[0]

slow_print("The encoded message is:")
print(encoded_message)
print("")

slow_print("Now, we will decode the message.")
slow_print("For that, we will call the De_Enigma function from the AlphaEncoder module, and use the permutation matrixes.")
slow_print("The keys are the same as before, otherwise the message would not be decoded.")
slow_print("The decoded message is:")

decoded_message = de_enigma(encoded_message, P, E)
print(decoded_message)
print("")

slow_print("As you can see, the message was encoded and decoded successfully.")
slow_print("Thank you for using the AlphaEncoder Project!")
slow_print("For more information, please visit the GitHub repository: https://github.com/thomaschiari/Algebra-Linear-Enigma")
