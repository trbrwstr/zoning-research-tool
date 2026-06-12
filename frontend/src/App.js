import React, { useState } from 'react';
import { Search, MapPin, FileText, AlertCircle, CheckCircle } from 'lucide-react';
import ZoningLookupForm from './components/ZoningLookupForm';
import ZoningResults from './components/ZoningResults';
import MapView from './components/MapView';
import PricingModal from './components/PricingModal';
import './App.css';

function App() {
  const [lookupResult, setLookupResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [showPricing, setShowPricing] = useState(false);
  const [pricingInfo, setPricingInfo] = useState(null);

  const handleLookup = async (address) => {
    setLoading(true);
    setError(null);
    setLookupResult(null);

    try {
      const response = await fetch('http://localhost:8000/api/zoning/lookup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ address }),
      });

      if (!response.ok) {
        throw new Error('Failed to lookup zoning information');
      }

      const data = await response.json();
      setLookupResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleShowPricing = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/pricing/info');
      const data = await response.json();
      setPricingInfo(data);
      setShowPricing(true);
    } catch (err) {
      console.error('Failed to fetch pricing:', err);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
      <nav className="bg-slate-900/50 backdrop-blur-lg border-b border-slate-700">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center space-x-2">
              <MapPin className="h-8 w-8 text-emerald-400" />
              <span className="text-xl font-bold text-white">Zoning Research Tool</span>
            </div>
            <button
              onClick={handleShowPricing}
              className="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg transition-colors"
            >
              View Pricing
            </button>
          </div>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="text-center mb-12">
          <h1 className="text-4xl md:text-5xl font-bold text-white mb-4">
            Instant Zoning & Permit Research
          </h1>
          <p className="text-xl text-slate-300 max-w-2xl mx-auto">
            Get comprehensive zoning summaries, setback requirements, and permit processes in seconds with AI-powered analysis
          </p>
        </div>

        <ZoningLookupForm onLookup={handleLookup} loading={loading} />

        {error && (
          <div className="mt-6 p-4 bg-red-900/50 border border-red-700 rounded-lg flex items-center space-x-2">
            <AlertCircle className="h-5 w-5 text-red-400" />
            <p className="text-red-200">{error}</p>
          </div>
        )}

        {lookupResult && (
          <div className="mt-8 grid grid-cols-1 lg:grid-cols-2 gap-8">
            <ZoningResults result={lookupResult} />
            <MapView 
              latitude={lookupResult.latitude} 
              longitude={lookupResult.longitude}
              geojson={lookupResult.geojson_data}
            />
          </div>
        )}
      </main>

      {showPricing && (
        <PricingModal 
          pricing={pricingInfo} 
          onClose={() => setShowPricing(false)} 
        />
      )}
    </div>
  );
}

export default App;
