export async function onRequest(context) {
  const { request, env } = context;
  const authHeader = request.headers.get("Authorization");

  const expectedUser = "linail";
  const expectedPass = env.SAYFA_SIFRESI;

  function unauthorized() {
    return new Response("Yetkisiz Erişim / Unauthorized", {
      status: 401,
      headers: {
        "WWW-Authenticate": 'Basic realm="Linail VIP", charset="UTF-8"',
        "Content-Type": "text/plain; charset=utf-8",
        "X-Robots-Tag": "noindex, nofollow"
      }
    });
  }

  if (!authHeader || !authHeader.startsWith("Basic ")) {
    return unauthorized();
  }

  try {
    const base64Credentials = authHeader.substring(6).trim();
    const decoded = atob(base64Credentials);
    const colonIndex = decoded.indexOf(":");
    if (colonIndex === -1) {
      return unauthorized();
    }
    const user = decoded.substring(0, colonIndex);
    const pass = decoded.substring(colonIndex + 1);

    if (!expectedPass || user !== expectedUser || pass !== expectedPass) {
      return unauthorized();
    }

    const response = await context.next();
    const newHeaders = new Headers(response.headers);
    newHeaders.set("X-Robots-Tag", "noindex, nofollow");

    return new Response(response.body, {
      status: response.status,
      statusText: response.statusText,
      headers: newHeaders
    });
  } catch (err) {
    return unauthorized();
  }
}
