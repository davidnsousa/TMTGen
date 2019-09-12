# TMTGen

TMTGen is an automatic [Trail Making Test](https://en.wikipedia.org/wiki/Trail_Making_Test) (TMT) generator for experimental research in neuropsychology.

The program offers a trail generator as well as a testing platform for measuring response speed and response accuracy in the TMT.

## Instructions

This repository contains a config file `config` and script `TMT_trail_gen.py` in the cfg directory that are necessary for generating the trails, and a main script `TMT.py` for testing participants.

Use python 3 to run the scripts.

To speed-test the program just run `TMT_trail_gen.py` followed by `TMT.py`.

### Generating trails

An example `config` file is provided in the cfg directory to generate the trail. Open the config file with a common text editor. This particular trail config file looks like follows:

	800
	600
	40
	2
	1 2 3
	1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
	Training Phase\n\n Tap \<spacebar> to continue
	Testing Phase\n\n Tap \<spacebar> to continue
	End\n\n \n\n Tap \<esc> to exit
	default


where the first two lines specify the size (in pixels) of the trail container in your screen; the 3rd, the size of the trail nodes; the 4th, the number of experiment phases; the 5th and 6th, the tags contained in the trail nodes for each experiment phase; the 7th and 8th, the opening messages for each experiment phase; the 9th, the closing message; the 10th, the name of the trail setup file to generate. Be sure to leave an empty line at the end of `config`. Also be sure not to leave any blank characters at the end of each line of the config file.

Run the `TMT_trail_gen.py` script in the cfg directory to generate the trail. This script will produce a new file `default` with all the information above plus the position in the screen of each randomly placed trail node. This way, you do not loose any information regarding the settings of the generated trail, and still can use the same primary config file and change it as you wish to create new experiments. Just make sure you give them different names. 

For another example, the config file of an experiment with two testing phases of numbers and letters would look like follows:

	800
	600
	40
	3
	1 2 3
	1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
	A B C D E F G H I J K L M N O P Q R S T U V X Z
	Training Phase\n\n Tap <spacebar> to continue
	Testing Phase 1\n\n Tap <spacebar> to continue
	Testing Phase 2\n\n Tap <spacebar> to continue
	End\n\n \n\n Tap \<esc> to exit
	default


Run the `TMT_trail_gen.py` script to generate this trail. 

### Testing participants

Run the `TMT.py` script to test participants. This script will open a fullscreen window with 5 input fields: *Id*, *Gender*, *Age* , *Trail* and *Condition*. Here you can specify, the identification code, gender and age of the participant, as well as the experiment condition and the TMT trail she will perform. The trail should have the same name as the trail file generated from the config file. Default input is provided to test the program. To continue click *Submit*. 

To perform the test, participants must click the trail nodes in the right order. By doing so, a line will appear connecting the nodes. Each test phase ends automatically when the trail is completed.

### Output

Upon the TMT completion an output `.csv` file is generated at the main TMTGen directory with the same name as the code specified in the participant's Id input field: `test.csv` as default.

The output data comes in long format. Each line is produced at each mouse click on a node tag. The following variables are presented: `Id`, `Gender`, `Age`, `Date`, `Trail`, `Condition`, `Level`, `Tag`, `Time` and `Correct`, where `Level` refers to the experiment phase, `Tag` refers to the node clicked, `Time` to the time elapsed since the beginning of the experiment (in seconds) and `Correct` to whether it was a correct response (`1`) or not (`0`).

## Citing

If you use TMTGen please cite the program with

## Contact

For further questions please contact davidnsousa@gmail.com.
