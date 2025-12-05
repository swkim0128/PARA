---
type: Template
archive: false
---
### 리팩토링 prompt

spring rabbitmq receiver 기능을 구현 중에 있어  
대략적인 receiver 함수 구성은 대략적으로 다음과 같아  

```Java
for (OesMessage oesMessage : messages) {
	List<OesItem> oesItems = oesMessage.getItems();
	logger.info("[action:{}][item:{}", oesMessage.getAction(), oesItems);

	for (OesItem item : oesItems) {
		try {
			if (!routingKey.equals(oesMessage.getAction())) {
				throw new MessageConversionException("PARAMETER ERROR!!!");
			}
			if (item.isNull()) {
				throw new MessageConversionException("PARAMETER ERROR!!!");
			}

			item.accept(visitor);
		}
		catch (NotFoundException e) {
			logger.error(String.format("[action:%s][item:%s] %s",
					oesMessage.getAction(), oesMessage.getItem(), e.getMessage()));
		}
		catch (Exception e) {
			// MessageConversionException 예외일 경우 메세지 버림
			logger.error(String.format("[action:%s][item:%s] %s",
					oesMessage.getAction(), oesMessage.getItem(), e.getMessage()));
			channel.basicNack(tag, false, false);
		}
	}
}
```

---

위 소스코드를 리팩토링하고 싶어