import api from './api';

export const aiService = {
  predictLevel: async (data) => (await api.post('/ai/predict-level', data)).data,
  getRecommendation: async () => (await api.get('/ai/recommendation')).data,
  getWeakSkills: async () => (await api.get('/ai/weak-skills')).data,
};
