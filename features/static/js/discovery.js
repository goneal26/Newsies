// discovery.js

// Example: Fetch news articles from an API and display them dynamically
document.addEventListener('DOMContentLoaded', async () => {
  try{
    const response = await fetch('https://api.example.com/news');
    const data = await response.json();

    const articlesContainer = document.querySelector('.news-articles');

    data.articles.forEach(article => {
      const articleElement = createArticleElement(article);
      articlesContainer.appendChild(articleElement);
    });
  } catch (error) {
    console.error('Error fetching news articles:', error);
  }
});

function createArticleElement(article) {
  const articleDiv = document.createElement('div');
  articleDiv.classList.add('news-article');

  const articleImage = document.createElement('img');
  articleImage.src = article.imageUrl;
  articleImage.alt = article.title;

  const articleTitle = document.createElement('h2');
  articleTitle.textContent = article.title;

  const articleContent = document.createElement('p');
  articleContent.textContent = article.description;

  const readMoreLink = document.createElement('a');
  readMoreLink.href = article.url;
  readMoreLink.textContent = 'Read More';

  articleDiv.appendChild(articleImage);
  articleDiv.appendChild(articleTitle);
  articleDiv.appendChild(articleContent);
  articleDiv.appendChild(readMoreLink);

  return articleDiv;
}

// Add more custom JavaScript functionality as needed
