let content = document.getElementById("text_content");
let wordCount = document.getElementById("word-count");



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

