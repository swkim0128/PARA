# PHP 수행시간 측정

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article4.6bc1851654a0.png)

## Metadata
- Author: [[zetawiki.com]]
- Full Title: PHP 수행시간 측정
- Category: #articles
- Document Tags: [[php]] 
- Summary: 10만회 수행한 시간을 측정해보자.
- URL: https://zetawiki.com/wiki/PHP_%EC%88%98%ED%96%89%EC%8B%9C%EA%B0%84_%EC%B8%A1%EC%A0%95

## Highlights
- function get_time() { return microtime(true); } $start = get_time(); /* 수행할 내용 */ $end = get_time(); $time = $end - $start; echo number_format($time, 8) . " 초 걸림"; ([View Highlight](https://read.readwise.io/read/01hfx470jdzz3mfjaqh724cx9j))
