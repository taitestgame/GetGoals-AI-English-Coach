import api from './api';

export const quizService = {
  getAll: async () => (await api.get('/quizzes')).data,
  getById: async (id) => (await api.get(`/quizzes/${id}`)).data,
  create: async (data) => (await api.post('/quizzes', data)).data,
  submit: async (id, answers) => (await api.post(`/quizzes/${id}/submit`, answers)).data,
};
