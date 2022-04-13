import Head from 'next/head'
import { useAuth } from '../contexts/auth'
import useResource from '../hooks/useResource'

export default function Home() {

    // const user = { username: 'roger'};
    const { user, login, logout } = useAuth();
    const { resources, loading } = useResource();


  return (
    <div>
        <Head>
            <title>Cookie Stand Demo</title>
            <link rel="icon" href="/favicon.ico" />
        </Head>

        <main className="p-4 space-y-8 text-center">
                <h1 className="text-4xl">Fetching Data from Authenticated API</h1>
                {user ? (
                    <>
                        <h2>Welcome {user.username}</h2>
                        <button onClick={logout} className="p-2 text-white bg-gray-500 rounded">Logout</button>
                        <StandList stands={resources} loading={loading} />
                    </>
                ) : (
                    <>
                        <h2>Need to log in</h2>
                        <button onClick={() => login(process.env.NEXT_PUBLIC_USERNAME, process.env.NEXT_PUBLIC_PASSWORD)} className="p-2 text-white bg-gray-500 rounded">Login</button>
                    </>
                )}
            </main>
    </div>
  )
}

function StandList({ stands, loading }) {

    if (loading) return <p>Loading...</p>

    return <ul>
        {stands.map(stand => (
            <li key={stand.id}>{stand.location}</li>
        ))}
    </ul>
}

