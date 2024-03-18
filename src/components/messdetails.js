import React, { useState } from 'react';

const MessDetails = () => {
  const [messDetails, setMessDetails] = useState('');
  const [sentiment, setSentiment] = useState('');

  const handleClick = async () => {
    // Assuming you have an API endpoint for fetching mess details and performing sentiment analysis
    const response = await fetch('http://localhost:5000/api/k/messdetails', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ messDetails }),
    });
    const data = await response.json();
    setSentiment(data.sentiment);
  };

  return (
    <div>
      <h6 className="mt-6 mb-0 ml-2">Mess Details</h6>
      <p className="ml-2 leading-normal text-sm">
        <span className="font-bold">Active</span> from Jan 23, 2023
      </p>
      {/* Input field for mess details */}
      <textarea
        className="w-full h-40 px-4 py-2 mt-4 border rounded-md"
        placeholder="Enter mess details..."
        value={messDetails}
        onChange={(e) => setMessDetails(e.target.value)}
      />
      {/* Button to trigger sentiment analysis */}
      <button
        className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded mt-2"
        onClick={handleClick}
      >
        Analyze Sentiment
      </button>
      {/* Display sentiment analysis result */}
      {sentiment && (
        <div className="mt-4">
          <h6>Sentiment Analysis Result:</h6>
          <p>{sentiment}</p>
        </div>
      )}
    </div>
  );
};

export default MessDetails;
