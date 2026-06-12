import React from 'react';
import { X, Check, Zap, Calendar } from 'lucide-react';

function PricingModal({ pricing, onClose }) {
  if (!pricing) return null;

  return (
    <div className="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div className="bg-slate-800 rounded-2xl border border-slate-700 max-w-4xl w-full max-h-[90vh] overflow-y-auto">
        <div className="p-6 border-b border-slate-700 flex justify-between items-center">
          <h2 className="text-2xl font-bold text-white">Choose Your Plan</h2>
          <button
            onClick={onClose}
            className="text-slate-400 hover:text-white transition-colors"
          >
            <X className="h-6 w-6" />
          </button>
        </div>

        <div className="p-6">
          <div className="grid md:grid-cols-2 gap-6">
            {/* Per Lookup Plan */}
            <div className="bg-slate-700/50 rounded-xl p-6 border border-slate-600 hover:border-emerald-500 transition-colors">
              <div className="flex items-center space-x-3 mb-4">
                <Zap className="h-8 w-8 text-emerald-400" />
                <div>
                  <h3 className="text-xl font-bold text-white">Per Lookup</h3>
                  <p className="text-slate-400 text-sm">Pay as you go</p>
                </div>
              </div>
              <div className="mb-6">
                <span className="text-4xl font-bold text-white">${pricing.price_per_lookup}</span>
                <span className="text-slate-400">/lookup</span>
              </div>
              <ul className="space-y-3 mb-6">
                <li className="flex items-center space-x-2 text-slate-300">
                  <Check className="h-5 w-5 text-emerald-400" />
                  <span>Instant zoning analysis</span>
                </li>
                <li className="flex items-center space-x-2 text-slate-300">
                  <Check className="h-5 w-5 text-emerald-400" />
                  <span>AI-powered interpretation</span>
                </li>
                <li className="flex items-center space-x-2 text-slate-300">
                  <Check className="h-5 w-5 text-emerald-400" />
                  <span>Property visualization</span>
                </li>
                <li className="flex items-center space-x-2 text-slate-300">
                  <Check className="h-5 w-5 text-emerald-400" />
                  <span>No commitment required</span>
                </li>
              </ul>
              <button className="w-full py-3 bg-emerald-600 hover:bg-emerald-700 text-white font-semibold rounded-lg transition-colors">
                Get Started
              </button>
            </div>

            {/* Monthly Subscription Plan */}
            <div className="bg-gradient-to-br from-emerald-900/50 to-slate-700/50 rounded-xl p-6 border-2 border-emerald-500 relative">
              <div className="absolute -top-3 right-4 bg-emerald-500 text-white text-sm font-bold px-3 py-1 rounded-full">
                POPULAR
              </div>
              <div className="flex items-center space-x-3 mb-4">
                <Calendar className="h-8 w-8 text-emerald-400" />
                <div>
                  <h3 className="text-xl font-bold text-white">Monthly</h3>
                  <p className="text-slate-400 text-sm">Best for frequent users</p>
                </div>
              </div>
              <div className="mb-6">
                <span className="text-4xl font-bold text-white">${pricing.monthly_subscription_price}</span>
                <span className="text-slate-400">/month</span>
              </div>
              <ul className="space-y-3 mb-6">
                <li className="flex items-center space-x-2 text-slate-300">
                  <Check className="h-5 w-5 text-emerald-400" />
                  <span>{pricing.monthly_lookups_included} lookups included</span>
                </li>
                <li className="flex items-center space-x-2 text-slate-300">
                  <Check className="h-5 w-5 text-emerald-400" />
                  <span>Everything in Per Lookup</span>
                </li>
                <li className="flex items-center space-x-2 text-slate-300">
                  <Check className="h-5 w-5 text-emerald-400" />
                  <span>Priority processing</span>
                </li>
                <li className="flex items-center space-x-2 text-slate-300">
                  <Check className="h-5 w-5 text-emerald-400" />
                  <span>API access</span>
                </li>
                <li className="flex items-center space-x-2 text-slate-300">
                  <Check className="h-5 w-5 text-emerald-400" />
                  <span>Save ${((pricing.price_per_lookup * pricing.monthly_lookups_included) - pricing.monthly_subscription_price).toFixed(2)}/month</span>
                </li>
              </ul>
              <button className="w-full py-3 bg-emerald-500 hover:bg-emerald-600 text-white font-semibold rounded-lg transition-colors">
                Subscribe Now
              </button>
            </div>
          </div>

          <div className="mt-6 text-center">
            <p className="text-slate-400 text-sm">
              All plans include detailed zoning analysis, setback requirements, height restrictions, 
              and AI-powered interpretations. Cancel anytime.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default PricingModal;
