import http from '../until/http'

const url = 'led'

const LedApi = {
  getLed: () => {
    return http.get(url)
  },
  createLed: (body) => {
    return http.post(url, body)
  },
  updatedLed: (id, body) => {
    return http.put(`${url}/update/${id}`, body);
  },
  deleteLed: (id) => {
    return http.delete(`url/${id}`)
  }
}
export default LedApi
