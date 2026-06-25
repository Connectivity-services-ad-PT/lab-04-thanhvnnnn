# Lab 04 Docker Evidence

## Docker image
image=[fit4110/team-notify:lab04] id=sha256:c516268e3e8dcb0219b30efc8023f5640f48355fcce4a3b822f0f3664b1bc6c0 created=2026-06-24T18:03:12.816774083Z


## docker ps
NAMES                         STATUS                            PORTS
codex-lab04-notify-evidence   Up 3 seconds (health: starting)   0.0.0.0:8014->8000/tcp, [::]:8014->8000/tcp


## GET /health
{
    "status":  "ok",
    "service":  "notification",
    "version":  "0.4.0",
    "dependencies":  {
                         "queue":  "mock-ready",
                         "sender":  "mock-ready"
                     }
}

## Container logs tail
INFO:     172.17.0.1:58380 - "GET /health HTTP/1.1" 200 OK

