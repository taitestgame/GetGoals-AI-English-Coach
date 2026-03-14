import api from './api';

export const resultService = {
  getMyResults: async () => (await api.get('/results')).data,
  getById: async (id) => (await api.get(`/results/${id}`)).data,
  getSummary: async () => (await api.get('/results/summary/me')).data,
};
