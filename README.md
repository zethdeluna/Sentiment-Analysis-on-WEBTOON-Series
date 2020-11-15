# Sentiment Analysis on WEBTOON Series: _My Giant Nerd Boyfriend_ by [fishball](https://www.webtoons.com/en/slice-of-life/my-giant-nerd-boyfriend/list?title_no=958)

[WEBTOON](https://www.webtoons.com/en/) is a popular platform for creators and storytellers to publish their original content for the world to see, for free! The website is home to thousands of creator-owned content with amazing, diverse visions from all over the world.
In particular, I have chosen to analyze one of my favorite series available on WEBTOON, [My Giant Nerd Boyfriend](https://www.webtoons.com/en/slice-of-life/my-giant-nerd-boyfriend/list?title_no=958), the artist of which goes by the name "fishball". In this project, I'll be performing a sentiment anaylsis on fishball's very first episode, based on all the comments posted by users who have read it.

## Conclusions

![wordcloud](https://github.com/zethdeluna/Sentiment-Analysis-on-WEBTOON-Series/blob/main/MGNB_common_comments.png)

* Based on the visual above we can see that the most commonly used words in the comments were "tall", "boyfriend", and "short. In general, the readers of My Giant Nerd Boyfriend Episode 1 have agreed that the artist's boyfriend is indeed very tall and most readers that commented also have a boyfriend that is much taller than they are. Many readers have also stated they relate to the artist's height, saying that they, too, are short. 
* One thing to note is that the artist is based in Malaysia. The word "asia" is another highly used word in the comments, which could indicate that many of the readers are also Asian and feel pride that an Asian artist is so popular on WEBTOON. 
* Lastly, scattered throughout the visual are words like "joy", "funny", "heart", and "love", meaning that the audience generally had a positive reaction towards the story.

Overall, the comments show that Episode 1 of My Giant Nerd Boyfriend is the beginning of a series that WEBTOON readers will find to be very relatable and put them in a good mood.

(The code can be viewed in the first file in this repository.)

## The Data

The data was scraped using the Python program available in this repository, titled `scrape_tall_boyfriend.py` (which should have really been named `scrape_giant_boyfriend.py` if I had been paying attention). There are about 15 comments per page, and less than 100 pages. In short, the scraper does the following:
1. The website and comments are accessed using a Selenium webdriver.
2. The scraper collects the comments and their respective post dates on the current comments page.
3. The webdriver clicks the next page.
4. Steps 2 and 3 are repeated until all of the comments are collected.
5. The data is then stored in a Pandas dataframe, which then saved the data as a `.csv` file titled `tall_boyfriend_comments.csv` that can be found in this repository (again, I should've used "giant" instead of "tall" but the difference isn't so important).

The data itself is pretty simple. It only has 2 columns: Column 1 contains the comments and Column 2 contains their respective post dates. The data has 1,466 rows, although I should note that there are 159 duplicate rows, which would reduce the number of rows to 1,307 after removing the duplicates.
