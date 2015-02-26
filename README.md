Quiz
----

### Introduction

The QGIS plugin "Quiz" reads the data-format GIFT used by moodle and
supports different question types (see below). It works on its own, it
hardly interacts with QGIS and doesnt need an internet connection at
all. However, it logs quiz scores and stores the for evaluation (in
schools etc).

Here a couple of use cases:

-   Quizzes are used primarily in geography classes, either for
    lecture-relevant topics or to get to know QGIS itself.
-   The plugin can be used for students to do tests or to practice /
    train.
-   A lecturer can discuss questions, while pupils follow him in trainig
    mode.
-   Multiple choice questions can be used to do surveys in classes.

Following software supports editing GIFT-files:

-   LibreOffice Writer with Templates (Hot Potatoes Homepage)
-   MS Excel with Makros
-   Moodle

### Quiz Syntax

A quiz consists of:

-   An optional //Title: block, which sets the title of the quiz
-   An optional //Instruction: block, which sets instructions for the
    quiz
-   An arbitrary amount of question-blocks, which have to be one of the
    following: \
    -   Picture Question:\
         A picture is displayed, along with a question with multiple
        possible answers regarding it. The picture must be in png
        format, has to be named the same as the correct answer, and
        should reside in the /quizzes/images directory.
    -   Text Question:\
         A simple text question with exactly one correct answer
    -   Multiple Choice Question:\
         Text question with multiple possible correct answers, that all
        can have individual weightage.
    -   Matching Question:\
         A question / instruction, followed by two rows of elements, of
        which always two have to be matched together.
    -   Fill In The Gap Question:\
         A fill in the gap question with an arbitrary amount of gaps
        that have to be filled.

These blocks have to be seperated by an empty line from eachother. When
the quiz is created, one can open it via the plugin. For an example of a
quiz with all question types look below.

### Instruction for creating a quiz

Goal of this instruction is to create an own quiz using opensource
software. After finishing, one can either use the quiz in moodle or in
QGIS.

#### The typical workflow of creating a quiz is:

-   Prepare software
-   Creating the quiz
-   Testing the quiz
-   Publishing the quiz

#### Preparation

A programming- or normal text-editor can be used to create a quiz. There
are templates for creating quizzes in LibreOffice\
 Additional preparation is not necessary.

#### Infos:

The question types are all also described in this
[GIFT-Documentation](http://docs.moodle.org/23/en/GIFT)

#### Creating a quiz

Use a simple editor to write a quiz.

#### Testing a quiz

Use this plugin or the Moodle-platform to test your quiz.

#### Quiz publizieren

Load your quiz to this
[Wiki-page](http://giswiki.hsr.ch/QGIS_Quiz_Plugin)

### Example of a quiz

       //Title:Example
       //Instruction:Answer the questions

       //Picture-Question
       ::Q1::Which country is being displayed?
       { ~Serbia
        =Afghanistan 
        ~Spain 
        }

       //Text-Question
       ::Q2::What's the capital of Islamabad?
       { =Islamabad ~Kabul ~Ulang Bator ~Doha ~Dehli ~Vientanne ~Riad }

       //Multiple-Choice
       ::Q3::These countries have a shared border with India:
       { ~%-100%Thailand ~%33%Bangla Desh ~%33%Pakistan ~%33%China }

       //Matching
       ::Q4::Match these countries with their capitals:
       {=Surinam -> Paramarimbo 
           =Andorra -> Andorra de la Ville 
           =China ->Peking 
           =Afghanistan -> Kabul }

       //Picture-Question
       ::Q5::Which country is being displayed?
       { ~Finnland ~Estonia =Lettland ~Albania }

       //Picture-Question
       ::Q6::Which country is this?
       { =Irland ~England ~France ~Ukraine }

       //Lückentext
       ::Q7::
       At the moment, 
       { 
       ~Iran =Indonesia ~Saudi Arabia ~Pakistan 
       }
        is the most populous country that's mainly muslim.
       Off course, south of it is
       {
        =Australia
        }
        .One can catch cangaroos there, using a 
       {
        =net
        }
        .

       //Picture-Question
       ::Q8::Which country is being displayed?
       {~Serbia 
           ~Kosovo 
           ~Germany
           =Bosnien}
