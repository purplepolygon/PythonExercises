# Coding Exercises


This is a repo that is used to destress or expand the mind.
The truth will set you free.

## About this repository

This is where I practice my algorithms and data structures.

If you are a prospective employer and would like to see my best work, I highly recommend you visit the Cracking the Coding Interview section of the repo.

That is currently my most recent and best work.

There are 4 sections:

### I. Cracking the coding interview

### II. MIT 6.0001

### III. Old - Codewars

### IV. Project Euler


## Future plans

I hope to constantly keep this repository updated throughout my career. I can't wait to see what it will look like in 10, 15, or 20 years!

Right now it's almost all python however I can code in Javascript or php as well. 

I'm debating whether or not to start making versions, but to be frank it seems a bit silly as this repo isn't really usable software in the traditional sense. I do like the idea of having a nice, beautiful repository but at the same time too much salt can ruin a dish as well. Especially since this is coursework essentially, though I do believe some of these functions may be utilized in the future. For instance, the MIT downpayment calculator is pretty nifty.

## Pre-Commit

### First Time
If you'd like to see the full pre-commit log the first time I ran it 8-29-2021 you can chexk the very bottom of this file. How fun! I think I'll be running this periodically to practice my style and make sure I have it down. It caught a few errors that, had I decided to refactor Euler's after refactoring my old directory, would have been avoided. 

Fix End of Files.........................................................Failed
14 files changed out of 73
- HOWEVER - 
Exactly half of those were .MD or .txt files which do not need the same specs. 

Trim Trailing Whitespace.................................................Failed
4 files changed out of 73
- HOWEVER -
1 of them was a .MD, and the other 3 came from MIT, not me =) !!

black....................................................................Failed
31 files changed out of 73

Black prettifier:
Definitely good to refresh format especially switching between languages. I forgot that additional parameters for if+and can be formatted as such:

```       -     if x == len(uncompressed_list) - 1 and uncompressed_list[x] == uncompressed_list[x - 1]:

          +  if (
                x == len(uncompressed_list) - 1
                and uncompressed_list[x] == uncompressed_list[x - 1]
            ):
```
Similar for matrices as well : 

```
Deleted: matrix = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']]\

Added:
matrix = [
    ["a", "b", "c", "d"],
    ["e", "f", "g", "h"],
    ["i", "j", "k", "l"],
    ["m", "n", "o", "p"],
]
```

Overall running pre-commit was great and I learned a good amount. I'll be adding more hooks as time goes and hopefully bring my ratio of errors down..

## Resources I recommend:

freecodecamp.org - Absolutely fantastic beginner resource. The short, concise lessons keep you engaged and give you bite sized chunks of data to process.
I still visit these tutorials from time to time especially if I'm a bit rusty or haven't used a particular language/framework in a while.

MIT Open Courseware - 6.0001 Introduction to Computer Science - A top resource from one of the top universities. Their video tutorials are great.

Cracking the Coding Interview Book by Gayle Laakmann McDowell - I recommend to use this book before doing any Leetcode or programming challenges.

https://automatetheboringstuff.com/ - Automate the Boring Stuff is absolutely fantastic. You can get things that could otherwise take hours or even days done in minutes.

Get 2-3 wins from a script you wrote and you'll be hooked!

## Full pre-commit log
```
(venv) ...\PythonExercises>pre-commit sample-config
 See https://pre-commit.com for more information
 See https://pre-commit.com/hooks.html for more hooks
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files

(venv) ...\PythonExercises>pre-commit install
pre-commit installed at .git\hooks\pre-commit

(venv) ...\PythonExercises>pre-commit install
pre-commit installed at .git\hooks\pre-commit

(venv) ...\PythonExercises>pre-commit run --all-files
[INFO] Initializing environment for https://github.com/pre-commit/pre-commit-hooks.
[INFO] Initializing environment for https://github.com/psf/black.
[INFO] Installing environment for https://github.com/pre-commit/pre-commit-hooks.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
[INFO] Installing environment for https://github.com/psf/black.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
Check Yaml...............................................................Passed
Fix End of Files.........................................................Failed
- hook id: end-of-file-fixer
- exit code: 1
- files were modified by this hook

Fixing Crack the coding interview/2 - Linked Lists/llcheck.py
Fixing Project Euler/euler3/euler_3.py
Fixing Crack the coding interview/1 - Arrays and Strings/one_away.py
Fixing MIT6.0001/README.MD
Fixing Project Euler/euler1/euler_1.py
Fixing Crack the coding interview/2 - Linked Lists/linked_list_partition.py
Fixing Project Euler/README.MD
Fixing Crack the coding interview/2 - Linked Lists/README.MD
Fixing Crack the coding interview/1 - Arrays and Strings/README.md
Fixing Old - Codewars/README.MD
Fixing Crack the coding interview/2 - Linked Lists/remove_duplicates.py
Fixing README.md
Fixing MIT6.0001/ProblemSet2/words.txt
Fixing Project Euler/euler10/euler_10.py

Trim Trailing Whitespace.................................................Failed
- hook id: trailing-whitespace
- exit code: 1
- files were modified by this hook

Fixing MIT6.0001/ProblemSet2/hangman.py
Fixing MIT6.0001/ProblemSet3/test_ps3.py
Fixing Old - Codewars/README.MD
Fixing MIT6.0001/ProblemSet3/ps3.py

black....................................................................Failed
- hook id: black
- files were modified by this hook

reformatted ...\PythonExercises\Crack the coding interview\1 - Arrays and Strings\compression.py
reformatted ...\PythonExercises\Crack the coding interview\1 - Arrays and Strings\matrix_rotate.py
reformatted ...\PythonExercises\Crack the coding interview\1 - Arrays and Strings\palindrome.py
reformatted ...\PythonExercises\Crack the coding interview\1 - Arrays and Strings\zero_matrix.py
reformatted ...\PythonExercises\Crack the coding interview\2 - Linked Lists\delete_middle_node.py
reformatted ...\PythonExercises\Crack the coding interview\2 - Linked Lists\linked_list_class.py
reformatted ...\PythonExercises\Crack the coding interview\1 - Arrays and Strings\one_away.py
reformatted ...\PythonExercises\Crack the coding interview\2 - Linked Lists\sum_linked_lists.py
reformatted ...\PythonExercises\MIT6.0001\ProblemSet1\Problem2A\ps1b.py
reformatted ...\PythonExercises\MIT6.0001\ProblemSet1\Problem1A\ps1a.py
reformatted ...\PythonExercises\MIT6.0001\ProblemSet1\Problem3A\ps1c.py
reformatted ...\PythonExercises\MIT6.0001\ProblemSet3\ps3.py
reformatted ...\PythonExercises\MIT6.0001\ProblemSet2\hangman.py
reformatted ...\PythonExercises\Old - Codewars\descending_order\descending_order.py
reformatted ...\PythonExercises\Old - Codewars\digit_sums\digit_sums.py
reformatted ...\PythonExercises\Old - Codewars\find_divisors\find_divisors.py
reformatted ...\PythonExercises\Old - Codewars\find_outlier\find_outlier.py
reformatted ...\PythonExercises\Old - Codewars\phone_number_format\phone_number_format.py
reformatted ...\PythonExercises\Old - Codewars\reverse_integer\reverse_integer.py
reformatted ...\PythonExercises\Old - Codewars\spinning\spinning.py
reformatted ...\PythonExercises\Old - Codewars\split_strings\split_strings.py
reformatted ...\PythonExercises\Old - Codewars\two_sum\two_sum.py
reformatted ...\PythonExercises\Old - Codewars\validate_pins\validate_pins.py
reformatted ...\PythonExercises\Project Euler\euler1\euler_1.py
reformatted ...\PythonExercises\MIT6.0001\ProblemSet3\test_ps3.py
reformatted ...\PythonExercises\Project Euler\euler4\euler_4.py
reformatted ...\PythonExercises\Project Euler\euler6\euler_6.py
reformatted ...\PythonExercises\Project Euler\euler7\euler_7.py
reformatted ...\PythonExercises\Project Euler\euler11\euler_11.py
reformatted ...\PythonExercises\Project Euler\euler9\euler_9.py
reformatted ...\PythonExercises\Project Euler\euler8\euler_8.py
All done! \u2728 \U0001f370 \u2728
31 files reformatted, 42 files left unchanged.
```
