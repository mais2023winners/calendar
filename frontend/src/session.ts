const getSessionData = () => {

    const sessionRaw = localStorage.getItem('session');
    const session = sessionRaw ? JSON.parse(sessionRaw) : null;

    if (session) {
        return JSON.parse(session);
    } else {
        return null;
    }

}