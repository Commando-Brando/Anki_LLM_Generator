## Overview

`A tool to easily generate Anki flash cards for any topics using a large language model.`

For a long time traditional school learning has severely lacked innovation in how classes are taught, students are test, and how students are taught to learn.

Being able to learn and retain information is a skill itself and there are lots of tools to help with this. One of the most popular tools is Anki, a flash card application that uses spaced repetition to help you learn and retain information.

Anki helped me a ton during my Computer Science undergrad and I am confident that flash card studying is one of the best ways to learn and retain information.

However, creating flash cards is a time consuming process and I wanted to create a tool that would make it easier to create flash cards for any topic.

This project aims to bridge that gap by using a large language model to generate flash cards for any topic.

## References

Anki's philosophy follows the practice of spaced repitition learning and active recall testing, read more about at the [Anki Background Page](https://docs.ankiweb.net/background.html). 

Previous academic papers on the topics of Anki, Spaced Repitition, & Recall Testing

[The effectiveness of computer-based spaced repetition in foreign language vocabulary instruction](https://www.jstor.org/stable/90014364)

[An Analysis of Anki Usage and Strategy of First-Year Medical Students in a Structure and Function Course](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9045547/)

[A Cohort Study Assessing the Impact of Anki as a Spaced Repetition Tool on Academic Performance in Medical School](https://link.springer.com/article/10.1007/s40670-023-01826-8)

[Enhanced Learning and Retention of Medical Knowledge Using the Mobile Flash card Application Anki](https://link.springer.com/article/10.1007/s40670-021-01386-9)

[Relearning and Retaining Personally-Relevant Words using Computer-Based Flashcard Software in Primary Progressive Aphasia](https://www.frontiersin.org/articles/10.3389/fnhum.2016.00561/full)

## Roadmap

### V0.0.1

- [ ] Create a simple CLI tool that takes in a topic and generates a flash card for that topic
- [ ] Allow the user to specify a path for a document that is to be read to generate the flash card
- [ ] Allow the user to specify the pages of a document to be used to generate the flash card


### Possible Future Features

- [ ] Allow the user to specify a URL to be used to generate the flash card
- [ ] Allow the user to specify specific topics from text to be used to generate the flash card
- [ ] Allow the user to select which generated flash cards are added to a deck
- [ ] Allow the user to specify a deck to add the generated flash cards to
- [ ] Create a web UI for the tool
- [ ] Allow flash cards to generated from different modalities (images, videos, audio, etc.)


## Possible Applications

- Student who does not have time to make flash cards can easily do so from any document that contains text
- Teacher/Professor can easily create flash cards for their students
- Language learning can greatly be accelerated and thereby used by any language teaching processes including the United States Military accelerated language learning programs
- In medical situations where a patient needs to relearn things or train their brain in certain ways for memory. Anki cards have been found to be helpful in helping patients with Aphasia

I think for a lot of college courses if flash cards were readily available for each course it could be a huge help for students. I think this tool could be a huge help for students who are struggling in a course and need a way to quickly learn and retain information.

## Contributing

If you would like to contribute then first off thanks for the help and then go to the issues tab and find an issue that you would like to work on or create a new one if you have an idea for a new feature.

### Getting Started

1. Fork the repo
2. Create Virtual Environment `python3 -m venv menv` 
3. Activate Virtual Environment `source menv/bin/activate`
4. Install dependencies `pip install -r requirements.txt`
