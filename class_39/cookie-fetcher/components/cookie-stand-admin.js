import { useState, useEffect } from 'react'
import useSWR from 'swr'
import { fetchWithToken } from '../services/data-fetcher'

export default function CookieStandAdmin({ token, onLogout, username }) {

    const url = 'https://cookie-stand-api.herokuapp.com/api/v1/cookie-stands/';

    const { data, error } = useSWR([url, token], fetchWithToken);

    const [cookieStands, setCookieStands] = useState([]);

    useEffect(() => {
        if (!data) return;
        setCookieStands(data);
    }, [data])

    if (error) return <h2>Ruh Roh</h2>
    if (!data) return <h2>Loading...</h2>

    return (
        <div className="w-1/2 p-8 mx-auto bg-gray-400">
            <header className="flex items-center justify-between py-4">
                <h1 className="text-4xl text-gray-50">Cookie Stands</h1>
                <p onClick={onLogout}>
                    {username}
                    <svg xmlns="http://www.w3.org/2000/svg" className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                    </svg>
                </p>
            </header>
            {cookieStands.map(stand => (

                <p key={stand.id}>

                    {stand.location}
                </p>

            ))}
        </div>
    );

}
