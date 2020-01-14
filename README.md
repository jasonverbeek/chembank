# chembank
CLI tool to store and search projects and chemical interractions

### implemented
- create an 'experiment' which explains starting ingredients, story about the process and a TL;DR version.
- replace variables within the experiment like `{{chemical.sulfuricacid37}}` to `37% Sulfuric Acid`

### example experiment
```
    {
        "title": "Making {{chemical.sulfuricacid98}} attempt 1",
        "date": ["y-m-d", "2020-01-11"],
        "required": ["200ml {{chemical.sulfuricacid37}}",
                     "Heat source",
                     "250ml+ borosilicate container (beaker/flask)"],
        "description": [
            "Setting up a heated stirring plate outside the backdoor.",
            "Aimed a fan to above the 500ml Erlenmeyers flask i had placed on the plate to get rid of fumes.",
            "I filled the flask with 200ml of {{chemical.sulfuricacid37}}.",
            "I did not add a stirring rod since it was very cold outside and stirring would cool down the liquid too much.",
            "It was near the end of the winter and still very cold out.",
            "The plate took about 30 minutes to propery heat and steam started escaping.",
            "This indicates that the concentration is being increased.",
            "About 2 hours into the process 100ml has boiled off.",
            "this led me to believe the concentration should be between 45-65% depending on how much of the acid boiled off with the water.",
            "It got too dark outside to safely continue this process.",
            "I turn off the heat, seal the flask with an hoursglass and place it on cold stone.",
            "I moved the unknown concentration of acid to a UV blocking container just to be sure."
        ],
        "tldr": [
            "setup heat source outside or in fumehood",
            "heat {{chemical.sulfuricacid37}} to 100C+",
            "boiled away 50% of liquid (100ml)",
            "had to stop the process due to darkness outside",
            "did not produce {{chemical.sulfuricacid98}} (but rather something between that and {{chemical.sulfuricacid37}})"
        ]
    }
 ```

### WIP
- new list/search with indexes
- use Experiment class and pre-format all values for search
- use indexes
- find s way to enhance indexes, potentially by moving every accessed entry to the top of the index, or sort by nr. of reads total, or mixed in segments of X(5?)

### TODO
- indexes
- chemicals
- linked data for chemical interactions/supplies
- chemical interactions
- and more
