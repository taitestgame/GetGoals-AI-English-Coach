import api from './api';

export const lessonService = {
  getAll: async () => (await api.get('/lessons')).data,
  getById: async (id) => (await api.get(`/lessons/${id}`)).data,
  create: async (data) => (await api.post('/lessons', data)).data,
  update: async (id, data) => (await api.put(`/lessons/${id}`, data)).data,
  delete: async (id) => (await api.delete(`/lessons/${id}`)).data,
};
