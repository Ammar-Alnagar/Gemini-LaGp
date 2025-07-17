from langgraph_sdk import get_sync_client

def main():
    # Initialize the client
    client = get_sync_client()

    # Define the assistant and thread IDs
    assistant_id = "agent"
    thread_id = "some-thread-id"

    # Define the input query
    query = "What is the latest news on AI?"

    # Stream the assistant's response
    for event in client.stream(
        assistant_id,
        thread_id,
        input={"messages": [("human", query)]},
    ):
        print(event)

if __name__ == "__main__":
    main()
