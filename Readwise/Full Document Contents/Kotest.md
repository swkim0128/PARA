# Kotest

![rw-book-cover](https://kotest.io/img/favicon.ico)

## Metadata
- Author: [[kotest.io]]
- Full Title: Kotest
- Category: #articles
- Summary: Kotest is a testing framework that lets you write simple and stylish tests in different ways. It supports data-driven testing to check many input cases easily. You can also customize test execution with settings like timeout, parallelism, and tags.
- URL: https://kotest.io/docs/framework/framework.html

## Full Document
[Skip to main content](https://kotest.io/docs/framework/framework.html#__docusaurus_skipToContent_fallback)

* 
* Introduction

Version: 5.9.x

### Introduction

![intro_gif](https://kotest.io/assets/images/intro_gif-41d4e868847b330dec1c3b60e500b4fb.gif)
[![version badge](https://img.shields.io/maven-central/v/io.kotest/kotest-framework-engine.svg?label=release)](https://search.maven.org/search?q=g:io.kotest%20OR%20g:io.kotest.extensions)[version badge](https://search.maven.org/search?q=g:io.kotest%20OR%20g:io.kotest.extensions)
[![version badge](https://img.shields.io/nexus/s/https/s01.oss.sonatype.org/io.kotest/kotest-framework-engine.svg?label=snapshot)](https://s01.oss.sonatype.org/content/repositories/snapshots/io/kotest/)[version badge](https://s01.oss.sonatype.org/content/repositories/snapshots/io/kotest/)
#### Test with Style[​](https://kotest.io/docs/framework/framework.html#test-with-style)

Write [simple and beautiful tests](https://kotest.io/docs/framework/writing-tests.html) using one of the available styles:

```
class MyTests : StringSpec({  
"length should return size of string" {  
"hello".length shouldBe 5  
}  
"startsWith should test for a prefix" {  
"world" should startWith("wor")  
}  
})  

```

Kotest allows tests to be created in several styles, so you can choose the style that suits you best.

#### Check all the Tricky Cases With Data Driven Testing[​](https://kotest.io/docs/framework/framework.html#check-all-the-tricky-cases-with-data-driven-testing)

Handle even an enormous amount of input parameter combinations easily with [data driven tests](https://kotest.io/docs/framework/datatesting/data-driven-testing.html):

```
class StringSpecExample : StringSpec({  
"maximum of two numbers" {  
forAll(  
row(1, 5, 5),  
row(1, 0, 1),  
row(0, 0, 0)  
) { a, b, max ->  
         Math.max(a, b) shouldBe max  
}  
}  
})  

```

#### Fine Tune Test Execution[​](https://kotest.io/docs/framework/framework.html#fine-tune-test-execution)

You can specify the number of invocations, parallelism, and a timeout for each test or for all tests. And you can group tests by tags or disable them conditionally. All you need is [`config`](https://kotest.io/docs/framework/project-config.html):

```
class MySpec : StringSpec({  
"should use config".config(timeout = 2.seconds, invocations = 10, threads = 2, tags = setOf(Database, Linux)) {  
// test here  
}  
})  

```

[Edit this page](https://github.com/kotest/kotest/blob/master/documentation/versioned_docs/version-5.9.x/framework/index.md)

[NextSetup](https://kotest.io/docs/framework/project-setup.html)
