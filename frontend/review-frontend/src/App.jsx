import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [reviews, setReviews] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchReviews = async () => {
      try {
        const response = await fetch('https://automated-whatsapp-review.onrender.com/api/reviews', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
          mode: 'cors',
        })
        if (!response.ok) throw new Error(`HTTP ${response.status}: ${response.statusText}`)
        const data = await response.json()
        const reviewList = Array.isArray(data) ? data : data.reviews || []
        setReviews(reviewList)
        setError(null)
      } catch (err) {
        console.error('Fetch error:', err)
        setError(err.message || 'Failed to fetch reviews')
        setReviews([])
      } finally {
        setLoading(false)
      }
    }

    fetchReviews()
  }, [])

  const formatDate = (dateString) => {
    if (!dateString) return 'N/A'
    try {
      return new Date(dateString).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      })
    } catch {
      return dateString
    }
  }

  const renderReviews = () => {
    return reviews.map((review, idx) => (
      <article key={review.id || idx} className="review-item">
        <div className="review-header">
          <div className="review-meta">
            <h3 className="user-name">{review.user_name || 'Anonymous'}</h3>
            <span className="product">{review.product_name || 'Product'}</span>
          </div>
          <time className="timestamp">{formatDate(review.created_at)}</time>
        </div>
        <p className="review-text">{review.product_review || 'No text provided'}</p>
        {review.contact_number && (
          <div className="review-meta-info">
            <span className="contact-hint">Contact: {review.contact_number}</span>
          </div>
        )}
      </article>
    ))
  }

  return (
    <div className="app-container">
      <header className="header">
        <h1>Reviews</h1>
        <p className="subtitle">Feedback from our customers</p>
      </header>

      <main className="main-content">
        {loading && (
          <div className="state-message loading">
            <div className="spinner"></div>
            <p>Loading reviews...</p>
          </div>
        )}

        {error && (
          <div className="state-message error">
            <p>⚠️ {error}</p>
          </div>
        )}

        {!loading && !error && reviews.length === 0 && (
          <div className="state-message empty">
            <p>No reviews available</p>
          </div>
        )}

        {!loading && !error && reviews.length > 0 && (
          <div className="reviews-container">
            <div className="reviews-list">
              {renderReviews()}
            </div>
          </div>
        )}
      </main>
    </div>
  )
}

export default App
