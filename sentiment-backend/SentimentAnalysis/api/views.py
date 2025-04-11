from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import json

import nltk
import spacy
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create your views here.

sia = SentimentIntensityAnalyzer()
nlp = spacy.load('en_core_web_sm')

class DoSentimentAnalysis(APIView):
    def post(self, request):
        try:
            # Log the raw request body
            print("Raw Request Body:", request.body)

            # Parse the JSON body
            data = json.loads(request.body)
            print("Parsed Data:", data)

            text = data.get('text', '')
            print("Extracted Text:", text)

            if not text:
                return JsonResponse({'error': 'Text field is required'}, status=400)

            sentiment_score = sia.polarity_scores(text)
            compound_score = sentiment_score['compound']
            if (compound_score >= 0.05):
                sentiment = "Positive"
            elif (compound_score <= -0.05):
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            results = {
                'Sentiment Scores': sentiment_score,    
                'Text': data,
                'Sentiment': sentiment,
                'Text_Compound': compound_score,
            }

            return JsonResponse({'Successful':results})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)