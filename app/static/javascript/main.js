let content = document.getElementById("text_content");
let wordCount = document.getElementById("word-count");
let pageTitle = document.title;





function displayCount(){
  let paragraph =content.value;
  console.log('content from form')
  console.log(paragraph)

  let words = paragraph.trim().split(" ");
  console.log("after split")
  console.log(words); //return the array
  let totalCount = words.length;
  wordCount.textContent = totalCount + " words";
  console.log('wordcount')
  console.log(wordCount)
};

content.addEventListener("input",displayCount);

// hidding the paragraph in the index.html file

function hideParagraph(){
  let indexParagraph = document.getElementById('indexParagraph');
  if(document.title !== "Home"){
    indexParagraph.removeAttribute("hidden")

  }}
document.addEventListener('DOMContentLoaded',hideParagraph );

// for the first article we display block so that its like the hero of the pageTitle, the rest get grid
function setArticleDisplayStyle() {
  const articles = document.querySelectorAll('#article article');
  for (let i = 0; i < articles.length; i++) {
    const articleId = parseInt(articles[i].getAttribute('article_id'));
    if (articleId === 1) {
      articles[i].classList.add('articleBlock');
      articles[i].classList.add('titleAbove');
      
    } else {
      articles[i].classList.add('articleInline');
      articles[i].classList.add('titleBelow');
    }
  }
}

document.addEventListener('DOMContentLoaded', setArticleDisplayStyle);
