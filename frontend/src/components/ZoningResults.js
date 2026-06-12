import React from 'react';
import { FileText, Building, Ruler, AlertTriangle, CheckCircle, Clock } from 'lucide-react';

function ZoningResults({ result }) {
  const interpretedData = result.interpreted_data || {};

  return (
    <div className="bg-slate-800/50 backdrop-blur-lg rounded-2xl border border-slate-700 overflow-hidden">
      <div className="p-6 border-b border-slate-700">
        <div className="flex items-center space-x-3 mb-4">
          <FileText className="h-6 w-6 text-emerald-400" />
          <h2 className="text-2xl font-bold text-white">Zoning Analysis</h2>
        </div>
        <div className="space-y-2">
          <p className="text-slate-300">
            <span className="font-semibold text-white">Address:</span> {result.address}
          </p>
          <p className="text-slate-300">
            <span className="font-semibold text-white">Zoning Code:</span> {result.zoning_code || 'Pending...'}
          </p>
        </div>
      </div>

      <div className="p-6 space-y-6">
        {interpretedData.summary && (
          <div className="bg-slate-700/50 rounded-xl p-4">
            <h3 className="font-semibold text-white mb-2 flex items-center space-x-2">
              <FileText className="h-4 w-4 text-emerald-400" />
              <span>Summary</span>
            </h3>
            <p className="text-slate-300">{interpretedData.summary}</p>
          </div>
        )}

        {interpretedData.setback_requirements && (
          <div>
            <h3 className="font-semibold text-white mb-3 flex items-center space-x-2">
              <Ruler className="h-4 w-4 text-emerald-400" />
              <span>Setback Requirements</span>
            </h3>
            <div className="grid grid-cols-2 gap-3">
              <div className="bg-slate-700/50 rounded-lg p-3">
                <p className="text-sm text-slate-400">Front</p>
                <p className="text-white font-medium">{interpretedData.setback_requirements.front || 'N/A'}</p>
              </div>
              <div className="bg-slate-700/50 rounded-lg p-3">
                <p className="text-sm text-slate-400">Rear</p>
                <p className="text-white font-medium">{interpretedData.setback_requirements.rear || 'N/A'}</p>
              </div>
              <div className="bg-slate-700/50 rounded-lg p-3">
                <p className="text-sm text-slate-400">Side</p>
                <p className="text-white font-medium">{interpretedData.setback_requirements.side || 'N/A'}</p>
              </div>
              <div className="bg-slate-700/50 rounded-lg p-3">
                <p className="text-sm text-slate-400">Notes</p>
                <p className="text-white font-medium text-sm">{interpretedData.setback_requirements.notes || 'None'}</p>
              </div>
            </div>
          </div>
        )}

        {interpretedData.height_restrictions && (
          <div>
            <h3 className="font-semibold text-white mb-3 flex items-center space-x-2">
              <Building className="h-4 w-4 text-emerald-400" />
              <span>Height Restrictions</span>
            </h3>
            <div className="grid grid-cols-2 gap-3">
              <div className="bg-slate-700/50 rounded-lg p-3">
                <p className="text-sm text-slate-400">Maximum Height</p>
                <p className="text-white font-medium">{interpretedData.height_restrictions.maximum_height || 'N/A'}</p>
              </div>
              <div className="bg-slate-700/50 rounded-lg p-3">
                <p className="text-sm text-slate-400">Stories</p>
                <p className="text-white font-medium">{interpretedData.height_restrictions.stories || 'N/A'}</p>
              </div>
            </div>
          </div>
        )}

        {interpretedData.lot_coverage && (
          <div>
            <h3 className="font-semibold text-white mb-3 flex items-center space-x-2">
              <Building className="h-4 w-4 text-emerald-400" />
              <span>Lot Coverage</span>
            </h3>
            <div className="grid grid-cols-3 gap-3">
              <div className="bg-slate-700/50 rounded-lg p-3">
                <p className="text-sm text-slate-400">Max Coverage</p>
                <p className="text-white font-medium">{interpretedData.lot_coverage.maximum_coverage || 'N/A'}</p>
              </div>
              <div className="bg-slate-700/50 rounded-lg p-3">
                <p className="text-sm text-slate-400">Impervious</p>
                <p className="text-white font-medium">{interpretedData.lot_coverage.impervious_surface || 'N/A'}</p>
              </div>
              <div className="bg-slate-700/50 rounded-lg p-3">
                <p className="text-sm text-slate-400">Open Space</p>
                <p className="text-white font-medium">{interpretedData.lot_coverage.open_space || 'N/A'}</p>
              </div>
            </div>
          </div>
        )}

        {interpretedData.permitted_uses && interpretedData.permitted_uses.length > 0 && (
          <div>
            <h3 className="font-semibold text-white mb-3 flex items-center space-x-2">
              <CheckCircle className="h-4 w-4 text-emerald-400" />
              <span>Permitted Uses</span>
            </h3>
            <div className="bg-slate-700/50 rounded-lg p-4">
              <ul className="space-y-2">
                {interpretedData.permitted_uses.map((use, index) => (
                  <li key={index} className="text-slate-300 flex items-start space-x-2">
                    <span className="text-emerald-400 mt-1">•</span>
                    <span>{use}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        )}

        {interpretedData.potential_issues && interpretedData.potential_issues.length > 0 && (
          <div>
            <h3 className="font-semibold text-white mb-3 flex items-center space-x-2">
              <AlertTriangle className="h-4 w-4 text-amber-400" />
              <span>Potential Issues</span>
            </h3>
            <div className="bg-amber-900/20 border border-amber-700 rounded-lg p-4">
              <ul className="space-y-2">
                {interpretedData.potential_issues.map((issue, index) => (
                  <li key={index} className="text-amber-200 flex items-start space-x-2">
                    <span className="text-amber-400 mt-1">•</span>
                    <span>{issue}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        )}

        {interpretedData.recommendations && interpretedData.recommendations.length > 0 && (
          <div>
            <h3 className="font-semibold text-white mb-3 flex items-center space-x-2">
              <CheckCircle className="h-4 w-4 text-blue-400" />
              <span>Recommendations</span>
            </h3>
            <div className="bg-blue-900/20 border border-blue-700 rounded-lg p-4">
              <ul className="space-y-2">
                {interpretedData.recommendations.map((rec, index) => (
                  <li key={index} className="text-blue-200 flex items-start space-x-2">
                    <span className="text-blue-400 mt-1">•</span>
                    <span>{rec}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        )}

        {!interpretedData.summary && (
          <div className="bg-slate-700/50 rounded-xl p-4 flex items-center space-x-3">
            <Clock className="h-5 w-5 text-amber-400 animate-spin" />
            <p className="text-slate-300">
              Detailed analysis in progress. Refresh page in a few moments for complete results.
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

export default ZoningResults;
