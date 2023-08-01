import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'

export const Single = () => {
  const [value, setValue] = useState({ song_name: '', song_image: '', song_added_time: '', song_artist_name: [], song_album_name: '', song_play_time: '', song_href: '' })
  const location = useLocation()
  const track_id = location.pathname.split('/')[2]

  useEffect(() => {
    const fetchValues = async () => {
      try {
        const result = await axios.get(`/api/track/${track_id}`)
        console.log(result.data)
        setValue(result.data[0])
      }
      catch (error) {
      }
    }
    fetchValues()
  }, [track_id])

  return (
    <div className='single'>

      
      <div className='flex-row'>
        <div className='image'>
          <img src={value.song_image.replace('4851', '1e02')} alt={value.song_name} />
        </div>
        <div className='details'>
          <div className='song-details'>
            <div className='song-title'>
              {value.song_name}
            </div>
            <div className='artist-name'>
              {value.song_artist_name}
            </div>
          </div>
          <div className='play-time'>
            {value.song_play_time}
          </div>
        </div>
      </div>
      <div className='ms-player'>
        <iframe src={`https://open.spotify.com/embed/track/${track_id}`}  allowTransparency={true} allow="encrypted-media"></iframe>
      </div>
    </div>
  )
}
