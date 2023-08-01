import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'


export const Top50 = () => {
  const [values, setValues] = useState([{ song_name: '', song_image: '', song_added_time: '', song_artist_name: [], song_album_name: '', song_play_time: '', song_href: '' }])
  const [track, setTrack] = useState('')

  const onSongClick = () => {
    setTrack('1')
  }

  useEffect(() => {
    const fetchValues = async () => {
      const val = await axios.get('/api/top50')
      console.log(val.data)
      setValues(val.data)
    }
    fetchValues()
  }, [])
  console.log(values)
  return (

    <div className='top50'>
      <div className='main-header'>
        <h1>
          Top 50 Songs Global
        </h1>
        <span>
          {values.length} Songs
        </span>
      </div>
      <div className='main'>
        <div className='title-row'><div>Sr. No</div>
          <div>#title</div>
          <div>No. of plays</div>
          <div>Album</div>
          <div>Play Time</div>
        </div>
        {values.map((value, key) => (
          <div className='row'>
            <div className='sr-no'>{key + 1}</div>
            <div className='a-item'>
              <div className='song-image'>
                <img src={value.song_image} alt="" />
              </div>
              <div className='details'>
                <Link to={`${value.song_href}`} className='song-name' >
                <div className='song-name'>{value.song_name}</div>
                </Link>
                <div className='artist-name'>{value.song_artist_name.join(', ')}</div>
              </div>
            </div>
            <div className='b-item'>
              <div>{value.song_added_time}</div>
            </div>
            <div className='c-item'>
              <div>{value.song_album_name}</div>
            </div>

            <div className='d-item'>
              <div>{value.song_play_time}</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
