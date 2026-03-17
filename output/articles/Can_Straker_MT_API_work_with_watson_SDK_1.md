---
title: "Can Straker MT API work with watson SDK?"
knowledge_base: "Globalization Help Center"
category: "CAITS"
subcategory: "mt api"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760068102"
source_url: "https://help.straker.ai/en/g11n/can-straker-mt-api-work-with-watson-sdk"
exported_at: "2026-03-17T11:28:22Z"
---

# Can Straker MT API work with watson SDK?

Straker MT API works well with watson SDK implementation with custom Authenticator.

```
package com.umaoka.wlt;  
import java.io.ByteArrayInputStream;  
import java.io.InputStreamReader;  
import java.io.Reader;  
import java.net.URI;  
import java.net.http.HttpClient;  
import java.net.http.HttpRequest;  
import java.net.http.HttpResponse;  
import java.net.http.HttpResponse.BodyHandlers;  
import java.time.Instant;  
import java.util.Base64;  
  
import com.google.common.base.Strings;  
import com.google.gson.Gson;  
import com.google.gson.annotations.SerializedName;  
import com.ibm.cloud.sdk.core.security.Authenticator;  
import okhttp3.Request.Builder;  
  
public class ClientCredentialsAuthenticator implements Authenticator {  
    private static final long REFRESH_BEFORE_SECS = 60L;  
    private String tokenUrl;  
    private String clientId;  
    private String secret;  
    private volatile String token;  
    private volatile Instant refreshTime = Instant.now(); // Refresh token 60 seconds before it actually expires  
  
    public ClientCredentialsAuthenticator(String tokenUrl, String clientId, String secret) {  
        this.tokenUrl = tokenUrl;  
        this.clientId = clientId;  
        this.secret = secret;  
    }  
  
    @Override  
    public void validate() {  
        if (Strings.isNullOrEmpty(tokenUrl)) {  
            throw new IllegalArgumentException("OAuth token endpoint is not configured.");  
        }  
        if (Strings.isNullOrEmpty(clientId)) {  
            throw new IllegalArgumentException("Missing client ID.");  
        }  
        if (Strings.isNullOrEmpty(secret)) {  
            throw new IllegalArgumentException("Missing secret.");  
        }  
    }  
  
    @Override  
    public String authenticationType() {  
        return Authenticator.AUTHTYPE_BEARER_TOKEN;  
    }  
  
    @Override  
    public void authenticate(Builder requestBuilder) {  
        Instant now = Instant.now();  
        if (token == null || now.isAfter(refreshTime)) {  
            synchronized (this) {  
                if (token == null || now.isAfter(refreshTime)) {  
                    String basicAuth = "Basic " + Base64.getEncoder().encodeToString((clientId + ":" + secret).getBytes());  
                    try {  
                        HttpClient client = HttpClient.newHttpClient();  
                        HttpRequest req = HttpRequest.newBuilder().uri(new URI(tokenUrl)).header("Authorization", basicAuth).header("Content-Type", "application/x-www-form-urlencoded").header("Accept", "application/json").POST(HttpRequest.BodyPublishers.ofString("grant_type=client_credentials")).build();  
                        HttpResponse<byte[]> resp = client.send(req, BodyHandlers.ofByteArray());  
                        Gson gson = new Gson();  
                        try (Reader reader = new InputStreamReader(new ByteArrayInputStream(resp.body()))) {  
                            TokenResponseBody tokenRespBody = gson.fromJson(reader, TokenResponseBody.class);  
                            token = tokenRespBody.accessToken;  
                            long expiresSec = Long.parseLong(tokenRespBody.expiresIn);  
                            refreshTime = now.plusSeconds(expiresSec - REFRESH_BEFORE_SECS);  
                        }  
                    } catch (Exception e) {  
                        throw new RuntimeException("Error while getting OAuth client credentials token.", e);  
                    }  
                }  
            }  
        }  
        requestBuilder.addHeader("Authorization", "Bearer " + token);  
    }  
  
    static class TokenResponseBody {  
        @SerializedName("access_token")  
        String accessToken;  
        @SerializedName("expires_in")  
        String expiresIn;  
        @SerializedName("token_type")  
        String tokenType;  
    }  
}
```

Note: `clientId`/`secret`  should be replaced with actual values.

Ouput -

```
{ "word_count": 2, "character_count": 12, "translations": [ { "translation": "こんにちは世界！" } ] }
```
