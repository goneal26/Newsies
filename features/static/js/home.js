// home.js

// Function to fetch and display news articles
function fetchNewsArticles() {
  // Implement logic to fetch news articles from an API or database and display them on the page
  // Example:
  // const articles = fetchArticlesFromAPI();
  // renderArticles(articles);
}

// Function to render individual news articles
function renderArticles(articles) {
  const main = document.querySelector('main');

  articles.forEach(article => {
    const articleElement = document.createElement('article');
    articleElement.classList.add('news-article');

    const img = document.createElement('img');
    img.src = article.imageUrl;
    img.alt = 'Article Image';
    articleElement.appendChild(h2);

    const h2 = document.createElement('h2');
    h2.textContent = article.title;
    articleElement.appendChild(h2);

    const p = document.createElement('p');
    p.textContent = article.summary;
    articleElement.appendChild(p);

    const readMoreLink = document.createElement('a');
    readMoreLink.href = article.link;
    readMoreLink.textContent = 'Read More';
    articleElement.appendChild(readMoreLink);

    main.appendChild(articleElement);
  });
}

// Call the fetchNewsArticles function when the page loads
document.addEventListener('DOMContentLoaded', fetchNewsArticles);
