import React, { useState } from 'react'
import BiensoxeApi from '../../../../Api/biensoxe'
import { useMutation, useQuery } from '@tanstack/react-query'
import { toast } from 'react-toastify'
import { useNavigate } from 'react-router-dom'
export default function RegisterLicense() {
  const navigate = useNavigate()
  const [dangkiBien, setDangkiBien] = useState({
    nguoidangki: '',
    mabien: ''
  })
  const mutateDangki = useMutation({
    mutationFn: (body) => BiensoxeApi.createBienso(body),
    onSuccess: () => {
      toast.success('Thêm thành công Biển số')
      navigate('/user')
    }
  })
  
  const handleSubmit = (event) => {
    // console.log('oki dki bien so')
    event.preventDefault()
    console.log(dangkiBien)
    mutateDangki.mutate(dangkiBien)
  }
  const handleChange = (event) => {
    const { name, value } = event.target
    setDangkiBien((prev) => {
      return {
        ...prev,
        [name]: value
      }
    })
  }
  return (
    <div className='w-full h-screen bg-gray-200 flex justify-center items-center'>
      <div className='p-5 w-[500px] bg-white rounded-lg shadow-lg'>
        <h1 className='text-center font-bold text-2xl mb-5'>Đăng Kí Biển Số</h1>
        <form className='space-y-4' onSubmit={handleSubmit}>
          <div className='flex flex-col'>
            <label htmlFor='ten-dang-ki' className='text-lg font-semibold'>
              Tên Đăng Kí
            </label>
            <input
              type='text'
              id='ten-dang-ki'
              name='nguoidangki'
              className='p-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500'
              value={dangkiBien.nguoidangki}
              onChange={handleChange}
            />
          </div>

          <div className='flex flex-col'>
            <label htmlFor='ma-bien' className='text-lg font-semibold'>
              Mã Biển
            </label>
            <input
              type='text'
              id='ma-bien'
              name='mabien'
              value={dangkiBien.mabien}
              className='p-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500'
              onChange={handleChange}
            />
          </div>

          <button
            type='submit'
            className='bg-blue-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline hover:bg-blue-600 transition duration-300'
          >
            Đăng Kí
          </button>
        </form>
      </div>
    </div>
  )
}
