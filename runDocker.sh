docker run -d --mount source=agraphvolume,target=/agraph/data -e AGRAPH_SUPER_USER=kingfisher -e AGRAPH_SUPER_PASSWORD=who-COOKS-for-you-2  -p 10000-10035:10000-10035 --shm-size 2g --name agraph --restart=always franzinc/agraph