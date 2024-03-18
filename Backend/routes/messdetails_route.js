const express = require('express');
const sentiment = require('sentiment');
const router = express.Router();

router.post('/messdetails', (req, res) => {
  const { messDetails } = req.body;

  // Perform sentiment analysis on the mess details
  const analysisResult = sentiment(messDetails);
  
  // Determine sentiment category based on score
  let sentimentCategory;
  if (analysisResult.score > 0) {
    sentimentCategory = 'positive';
  } else if (analysisResult.score < 0) {
    sentimentCategory = 'negative';
  } else {
    sentimentCategory = 'neutral';
  }

  // Return the sentiment category as the result
  res.json({ sentiment: sentimentCategory });
});

module.exports = router;
