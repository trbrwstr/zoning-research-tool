import React, { useState } from 'react';
import { Search, Loader2 } from 'lucide-react';

function ZoningLookupForm({ onLookup, loading }) {
  const [address, setAddress] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (address.trim()) {
      onLookup(address);
    }
  };

  return (
    <div className="max-w-2xl mx-auto">
      <form onSubmit={handleSubmit} className="relative">
        <div className="flex space-x-4">
          <div className="flex-1 relative">
            <Search className="absolute left-4 top-1/2 transform -translate-y-1/2 h-5 w-5 text-slate-400" />
            <input
              type="text"
              value={address}
              onChange={(e) => setAddress(e.target.value)}
              placeholder="Enter property address (e.g., 123 Main St, City, State)"
              className="w-full pl-12 pr-4 py-4 bg-slate-800 border border-slate-600 rounded-xl text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent text-lg"
              disabled={loading}
            />
          </div>
          <button
            type="submit"
            disabled={loading || !address.trim()}
            className="px-8 py-4 bg-emerald-600 hover:bg-emerald-700 disabled:bg-slate-600 disabled:cursor-not-allowed text-white font-semibold rounded-xl transition-colors flex items-center space-x-2"
          >
            {loading ? (
              <>
                <Loader2 className="h-5 w-5 animate-spin" />
                <span>Analyzing...</span>
              </>
            ) : (
              <>
                <Search className="h-5 w-5" />
                <span>Research</span>
              </>
            )}
          </button>
        </div>
      </form>
      <p className="mt-4 text-sm text-slate-400 text-center">
        Enter any US address to get comprehensive zoning and permit information
      </p>
    </div>
  );
}

export default ZoningLookupForm;
